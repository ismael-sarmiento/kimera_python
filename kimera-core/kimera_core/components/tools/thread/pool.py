from concurrent.futures.thread import ThreadPoolExecutor

from kimera_core.components.storage.dynamic.cache.local.engines import InMemoryCacheEngine
from kimera_core.components.tools.hash.md5 import build_hash


# Decorator by Cache
def thread_pool_executor_cache(decorated_function):
    """
        Schedules the callable to be executed as fn(*args, **kwargs).

        ThreadPoolExecutor(max_workers).submit(function, *args, **kwargs)
        :return: [Function] A future instance representing the execution of the callable.

    :return: [String] Unique Key (hash) of the future [function] cached of memory [InMemoryCacheEngine().get(key)]
    """

    def thread_pool_executor_function(*args, **kwargs):
        key = build_hash(decorated_function, args, kwargs)
        value = ThreadPoolExecutor(max_workers=5).submit(decorated_function, *args, **kwargs)
        InMemoryCacheEngine().set(key, value)
        return key

    return thread_pool_executor_function


# Decorator by Callback
def thread_pool_executor_callback(callback):
    """
        Attaches a callable that will be called when the future decorate finishes.

    :param callback: A callable that will be called with this future as its only argument when the future completes or is cancelled. The callable
                     will always be called by a thread in the same process in which it was added. If the future has already completed or been
                     cancelled then the callable will be called immediately. These callables are called in the order that they were added.
    :return: [String] Unique Key (hash) of the future [function] cached of memory [InMemoryCacheEngine().get(key)]
    """

    def thread_pool_executor(decorated_function):
        def thread_pool_executor_function(*args, **kwargs):
            key = build_hash(decorated_function, args, kwargs)
            future = ThreadPoolExecutor(max_workers=5).submit(decorated_function, *args, **kwargs)
            future.add_done_callback(callback)
            InMemoryCacheEngine().set(key, future)
            return key

        return thread_pool_executor_function

    return thread_pool_executor
