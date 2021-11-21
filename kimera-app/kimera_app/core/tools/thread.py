import threading
from concurrent.futures import ThreadPoolExecutor

import time

from kimera_core.components.storage.dynamic.cache.local.engines import ThreadCacheEngine
from kimera_core.components.tools.thread.pool import thread_pool_executor_callback


def my_callback_function(future):
    # print(f"CALLBACK FUNCTION - args: {args}")
    # print(f"CALLBACK FUNCTION - kwargs: {kwargs}")
    print(f"RESULT: {future.result()}")


@thread_pool_executor_callback(my_callback_function)
def function_by_decorator(*args, **kwargs):
    print("Executing Task: {} in {} seconds".format(kwargs['name'], kwargs['seconds']))
    print("args = {}, kwargs = {}".format(args, kwargs))
    time.sleep(kwargs['seconds'])
    print("Task Executed {} - {} seconds".format(threading.current_thread(), kwargs['seconds']))
    return kwargs['name']


def function_basic(*args, **kwargs):
    print("Executing Task: {} in {} seconds".format(kwargs['name'], kwargs['seconds']))
    print("args = {}, kwargs = {}".format(args, kwargs))
    time.sleep(kwargs['seconds'])
    print("Task Executed {} - {} seconds".format(threading.current_thread(), kwargs['seconds']))
    return kwargs['name']


def process_multi_thread_basic():
    print("\n\tStarting MultiThreadPool Basic ...")
    executor = ThreadPoolExecutor(max_workers=3)
    future = executor.submit(function_basic, (2), **{'name': 'functionI', 'seconds': 3})
    future = executor.submit(function_basic, (9), **{'name': 'functionII', 'seconds': 9})
    future = executor.submit(function_basic, (1), **{'name': 'functionIII', 'seconds': 1})
    # print(future.done())  # el proceso a terminado o no
    # future.result()  # ejecuta el proceso si o si
    print("All tasks complete")


def process_multi_thread_by_decorator():
    print("\n\tStarting MultiThreadPool By Decorator ...")
    future = function_by_decorator(name='functionI', seconds=3)
    future = function_by_decorator(name='functionII', seconds=9)
    future = function_by_decorator(name='functionIII', seconds=1)
    future = function_by_decorator(name='functionIV', seconds=2)
    print("All Tasks complete")


if __name__ == '__main__':
    # -------------------------------------------------------------------
    # ------------------------- EXAMPLES --------------------------------
    # -------------------------------------------------------------------
    # process_multi_thread_basic()
    process_multi_thread_by_decorator()
    ThreadCacheEngine()
    print("OK")
