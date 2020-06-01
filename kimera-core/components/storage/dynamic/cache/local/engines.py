""" This module contains different implementations from local caching """

import threading
from abc import ABC, abstractmethod
from time import time


class BaseCacheEngine(ABC):
    """ Abstract class of Base Cache """

    DEFAULT_TIMEOUT = 300.0  # seconds
    DEFAULT_SIZE = 300  # max elements in cache

    @abstractmethod
    def get(self, key: str) -> object:
        """
            Method to return the value of the key stored in the local cache.
            If this key does not exist it will return a null value.

        :param key: Key stored in local cache.
        :return: [object] Value of key.
        """

    @abstractmethod
    def set(self, key: str, value: object, timeout: float, size: int) -> None:
        """
            Method that update or create a pair {key:value} in local cache for a limited time.

        :param key: Key to update or create.
        :param value: Value to update or create.
        :param timeout: Value that represents the time (in seconds) of permanence of the pair {key:value}.
        :param size: Maximum number of objects in cache.
        """

    @abstractmethod
    def delete(self, key: str) -> None:
        """
            Method must that delete the value of existing key in local cache.

        :param key: Key to find.
        """

    @abstractmethod
    def exists(self, key: str) -> bool:
        """
            Method to return the existence or not in the local cache of a key.

        :param key: Key to find.
        :return: [bool] Existence or not int the local cache of a key.
        """

    @abstractmethod
    def clear(self) -> None:
        """
            Method that clear all cache.
        """


class LocalCacheEngine(BaseCacheEngine):
    """ Subclass class of Base Cache """

    @abstractmethod
    def size_regulator(self, size: int) -> None:
        """
            Method that regulates the size of the cache.

        :param size: Maximum number of objects in cache.
        """

    def normalize_timeout(self, timeout: float) -> float:
        """
            Method that returns the normalized timeout [seconds since the Epoch].

        :param timeout:  Value that represents the maximum time allowed (in seconds) of permanence of the pair {key:value}.
        :return: [Float] Normalized timeout
        """
        timeout = float(timeout) if timeout else self.DEFAULT_TIMEOUT
        return time() + timeout

    def normalize_size(self, size: int) -> int:
        """
            Method that returns the normalized cache size.

        :param size:  Maximum number of objects in cache.
        :return: [Int] Normalized cache size.
        """
        size = int(size) if size else self.DEFAULT_SIZE
        return size


class InMemoryCacheEngine(LocalCacheEngine):
    """ Subclass of Local Cache - Cache in Memory """

    def __init__(self):
        self.memory_cache = dict()

    def get(self, key):
        result = self.memory_cache.get(key)
        return result['value'] if result and result['timeout'] > time() else self.delete(key)

    def set(self, key, value, timeout=None, size=None):
        self.size_regulator(self.normalize_size(size))
        self.memory_cache[key] = {'timeout': self.normalize_timeout(timeout), 'value': value}

    def exists(self, key):
        return True if key in self.memory_cache and self.memory_cache[key]['timeout'] > time() else False

    def delete(self, key):
        if self.exists(key):
            del self.memory_cache[key]

    def clear(self):
        self.memory_cache = {}

    def size_regulator(self, size):
        if len(self.memory_cache) > size:
            count = len(self.memory_cache) - size
            list(map(lambda i: self.memory_cache.popitem(), range(count)))


class ThreadCacheEngine(LocalCacheEngine):
    """ Subclass of Local Cache - Cache in Current Thread """

    def _get_thread_local_cache(self) -> dict:
        """
            Method that returns the cache object of the current thread.

        :return: [Dict] Cache of current thread.
        """
        try:
            return threading.currentThread().thread_local_cache
        except AttributeError:
            self.clear()
            return threading.currentThread().thread_local_cache

    def get(self, key):
        result = self._get_thread_local_cache().get(key)
        return result['value'] if result and result['timeout'] > time() else self.delete(key)

    def set(self, key, value, timeout=None, size=None):
        self.size_regulator(self.normalize_size(size))
        self._get_thread_local_cache()[key] = {'timeout': self.normalize_timeout(timeout), 'value': value}

    def exists(self, key):
        return True if key in self._get_thread_local_cache() and self._get_thread_local_cache()[key]['timeout'] > time() else False

    def delete(self, key):
        if self.exists(key):
            del self._get_thread_local_cache()[key]

    def clear(self):
        threading.currentThread().thread_local_cache = {}

    def size_regulator(self, size):
        if len(self._get_thread_local_cache()) > size:
            count = len(self._get_thread_local_cache()) - size
            list(map(lambda i: self._get_thread_local_cache().popitem(), range(count)))


# Decorators
def thread_local_cache(key, timeout=None, size=None):
    def thread_local_cache_decorator(function):
        def thread_local_cache_decorator_function(*args, **kwargs):
            value = function(*args, **kwargs)
            ThreadCacheEngine().set(key, value, timeout, size)
            return value

        return thread_local_cache_decorator_function

    return thread_local_cache_decorator


# TODO: para que funcione la clase InMemoryCacheEngine debe ser Singleton
def in_memory_local_cache(key, timeout=None, size=None):
    def in_memory_local_cache_decorator(function):
        def in_memory_local_cache_decorator_function(*args, **kwargs):
            value = function(*args, **kwargs)
            InMemoryCacheEngine().set(key, value, timeout, size)
            return value

        return in_memory_local_cache_decorator_function

    return in_memory_local_cache_decorator


if __name__ == '__main__':
    # -------------------------------------------------------------------
    # ------------------------- EXAMPLES --------------------------------
    # -------------------------------------------------------------------

    # -------------------------------------------------------------------
    # IN MEMORY LOCAL CACHE
    # -------------------------------------------------------------------
    print("\n\t In Memory Local Cache Class - Example\n")
    key_1 = "key_1"
    key_2 = "key_2"
    key_3 = "key_3"
    in_memory_cache = InMemoryCacheEngine()
    print(f"Add new keys: {key_1}, {key_2}, {key_3}")
    in_memory_cache.set(key_1, "value1")
    in_memory_cache.set(key_2, "value2")
    in_memory_cache.set(key_3, "value3")
    print(f"\t\t{key_1} exists: {in_memory_cache.exists(key_1)}")
    print(f"\t\t{key_2} exists: {in_memory_cache.exists(key_2)}")
    print(f"\t\t{key_3} exists: {in_memory_cache.exists(key_3)}")
    print(f"Delete key: {key_1}")
    in_memory_cache.delete(key_1)
    print(f"\t\t{key_1} exists: {in_memory_cache.exists(key_1)}")
    print(f"\t\t{key_2} exists: {in_memory_cache.exists(key_2)}")
    print(f"\t\t{key_3} exists: {in_memory_cache.exists(key_3)}")
    print("Clear Local Cache")
    in_memory_cache.clear()
    print(f"\t\t{key_1} exists: {in_memory_cache.exists(key_1)}")
    print(f"\t\t{key_2} exists: {in_memory_cache.exists(key_2)}")
    print(f"\t\t{key_3} exists: {in_memory_cache.exists(key_3)}")

    # -------------------------------------------------------------------
    # THREAD LOCAL CACHE
    # -------------------------------------------------------------------
    print("\n\t Thread Local Cache Class - Example\n")
    key_1 = "key_1"
    key_2 = "key_2"
    key_3 = "key_3"
    print(f"Add new keys: {key_1}, {key_2}, {key_3}")
    ThreadCacheEngine().set(key_1, "value1")
    ThreadCacheEngine().set(key_2, "value2")
    ThreadCacheEngine().set(key_3, "value3")
    print(f"\t\t{key_1} exists: {ThreadCacheEngine().exists(key_1)}")
    print(f"\t\t{key_2} exists: {ThreadCacheEngine().exists(key_2)}")
    print(f"\t\t{key_3} exists: {ThreadCacheEngine().exists(key_3)}")
    print(f"Delete key: {key_1}")
    ThreadCacheEngine().delete(key_1)
    print(f"\t\t{key_1} exists: {ThreadCacheEngine().exists(key_1)}")
    print(f"\t\t{key_2} exists: {ThreadCacheEngine().exists(key_2)}")
    print(f"\t\t{key_3} exists: {ThreadCacheEngine().exists(key_3)}")
    print("Clear Local Cache")
    ThreadCacheEngine().clear()
    print(f"\t\t{key_1} exists: {ThreadCacheEngine().exists(key_1)}")
    print(f"\t\t{key_2} exists: {ThreadCacheEngine().exists(key_2)}")
    print(f"\t\t{key_3} exists: {ThreadCacheEngine().exists(key_3)}")

    # -------------------------------------------------------------------
    # DECORATOR
    # -------------------------------------------------------------------
    print("\n\t Thread Local Cache Decorator - Example\n")
    key_4 = "key_4"


    @thread_local_cache(key_4)
    def my_function(value):
        return value


    print(f"Add new key: {key_4} from decorator")
    my_function("value_4")
    print(f"Execute function: {my_function.__name__}")
    print(f"\t\t{key_4} exist: {ThreadCacheEngine().exists(key_4)}")
    print(f"Delete key: {key_4}")
    ThreadCacheEngine().delete(key_4)
    print(f"\t\t{key_4} exist: {ThreadCacheEngine().exists(key_4)}")

    # -------------------------------------------------------------------
    # DOC TEST
    # -------------------------------------------------------------------
    import doctest

    doctest.testmod()
