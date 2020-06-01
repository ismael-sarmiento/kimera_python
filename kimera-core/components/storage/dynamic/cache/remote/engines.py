""" This module contains different implementations from remote caching """

from abc import ABC, abstractmethod

from components.tools.utils._import import ImportUtils


class BaseCacheEngine(ABC):
    """ Abstract class of Base Cache """

    DEFAULT_TIMEOUT = 300.0
    DEFAULT_MAXSIZE = 300

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


class MemcachedEngine(BaseCacheEngine):

    def __init__(self):
        ImportUtils.raise_exception_if_module_not_exists('pymemcache')
        from pymemcache.client import base
        self._client = base.Client(('localhost', 11211))

    def get(self, key):
        return self._client.get(key)

    def exists(self, key):
        return self.get(key) is not None

    def set(self, key, value, timeout=None, size=None):
        return self._client.set(key, value)  # TODO: falta pasarle la configuracion

    def clear(self):
        return self._client.flush_all()

    def delete(self, key):
        return self._client.delete(key)

    def close(self):
        self._client.close()


class RedisEngine(BaseCacheEngine):

    def __init__(self):
        ImportUtils.raise_exception_if_module_not_exists('redis')
        import redis
        self._redis = redis.Redis()

    def get(self, key):
        return self._redis.get(key)

    def exists(self, key):
        return self.get(key) is not None

    def set(self, key, value, timeout=None, size=None):
        return self._redis.set(key, value, timeout)

    def clear(self):
        return self._redis.flushall()

    def delete(self, key):
        return self._redis.delete(key)

    def close(self):
        self._redis.close()


if __name__ == '__main__':
    # -------------------------------------------------------------------
    # ------------------------- EXAMPLES --------------------------------
    # -------------------------------------------------------------------
    # TODO: falta añadir un memcache real y los test
    # -------------------------------------------------------------------
    # MEMCACHE CACHE
    # -------------------------------------------------------------------
    print("\n\t Memcache Cache Class - Example\n")
    key_1 = "key_1"
    key_2 = "key_2"
    key_3 = "key_3"
    mem_cache = MemcachedEngine()
    print(f"Add new keys: {key_1}, {key_2}, {key_3}")
    mem_cache.set(key_1, "value1")
    mem_cache.set(key_2, "value2")
    mem_cache.set(key_3, "value3")
    print(f"\t\t{key_1} exists: {mem_cache.exists(key_1)}")
    print(f"\t\t{key_2} exists: {mem_cache.exists(key_2)}")
    print(f"\t\t{key_3} exists: {mem_cache.exists(key_3)}")
    print(f"Delete key: {key_1}")
    mem_cache.delete(key_1)
    print(f"\t\t{key_1} exists: {mem_cache.exists(key_1)}")
    print(f"\t\t{key_2} exists: {mem_cache.exists(key_2)}")
    print(f"\t\t{key_3} exists: {mem_cache.exists(key_3)}")
    print("Clear Local Cache")
    mem_cache.clear()
    print(f"\t\t{key_1} exists: {mem_cache.exists(key_1)}")
    print(f"\t\t{key_2} exists: {mem_cache.exists(key_2)}")
    print(f"\t\t{key_3} exists: {mem_cache.exists(key_3)}")

    # TODO: falta añadir un redis real y los test
    # -------------------------------------------------------------------
    # REDIS CACHE
    # -------------------------------------------------------------------
    print("\n\t Redis Cache Class - Example\n")
    key_1 = "key_1"
    key_2 = "key_2"
    key_3 = "key_3"
    redis_cache = RedisEngine()
    print(f"Add new keys: {key_1}, {key_2}, {key_3}")
    redis_cache.set(key_1, "value1")
    redis_cache.set(key_2, "value2")
    redis_cache.set(key_3, "value3")
    print(f"\t\t{key_1} exists: {redis_cache.exists(key_1)}")
    print(f"\t\t{key_2} exists: {redis_cache.exists(key_2)}")
    print(f"\t\t{key_3} exists: {redis_cache.exists(key_3)}")
    print(f"Delete key: {key_1}")
    redis_cache.delete(key_1)
    print(f"\t\t{key_1} exists: {redis_cache.exists(key_1)}")
    print(f"\t\t{key_2} exists: {redis_cache.exists(key_2)}")
    print(f"\t\t{key_3} exists: {redis_cache.exists(key_3)}")
    print("Clear Local Cache")
    redis_cache.clear()
    print(f"\t\t{key_1} exists: {redis_cache.exists(key_1)}")
    print(f"\t\t{key_2} exists: {redis_cache.exists(key_2)}")
    print(f"\t\t{key_3} exists: {redis_cache.exists(key_3)}")
