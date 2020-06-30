from kimera_core.components.storage.dynamic.cache.local.engines import InMemoryCacheEngine, in_memory_local_cache

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
    print(f"Add new keys: {key_1}, {key_2}, {key_3}")
    InMemoryCacheEngine().set(key_1, "value1")
    InMemoryCacheEngine().set(key_2, "value2")
    InMemoryCacheEngine().set(key_3, "value3")
    print(f"\t\t{key_1} exists: {InMemoryCacheEngine().exists(key_1)}")
    print(f"\t\t{key_2} exists: {InMemoryCacheEngine().exists(key_2)}")
    print(f"\t\t{key_3} exists: {InMemoryCacheEngine().exists(key_3)}")
    print(f"Delete key: {key_1}")
    InMemoryCacheEngine().delete(key_1)
    print(f"\t\t{key_1} exists: {InMemoryCacheEngine().exists(key_1)}")
    print(f"\t\t{key_2} exists: {InMemoryCacheEngine().exists(key_2)}")
    print(f"\t\t{key_3} exists: {InMemoryCacheEngine().exists(key_3)}")
    print("Clear Local Cache")
    InMemoryCacheEngine().clear()
    print(f"\t\t{key_1} exists: {InMemoryCacheEngine().exists(key_1)}")
    print(f"\t\t{key_2} exists: {InMemoryCacheEngine().exists(key_2)}")
    print(f"\t\t{key_3} exists: {InMemoryCacheEngine().exists(key_3)}")

    # -------------------------------------------------------------------
    # DECORATOR
    # -------------------------------------------------------------------
    print("\n\t In Memory Cache Decorator - Example\n")
    key_4 = "key_4"


    @in_memory_local_cache(key_4)
    def my_function(value):
        return value


    print(f"Add new key: {key_4} from decorator")
    my_function("value_4")
    print(f"Execute function: {my_function.__name__}")
    print(f"\t\t{key_4} exist: {InMemoryCacheEngine().exists(key_4)}")
    print(f"Delete key: {key_4}")
    InMemoryCacheEngine().delete(key_4)
    print(f"\t\t{key_4} exist: {InMemoryCacheEngine().exists(key_4)}")
