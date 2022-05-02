from kimera_core.components.storage.dynamic.cache.local.engines import ThreadCacheEngine, thread_local_cache

if __name__ == '__main__':
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
