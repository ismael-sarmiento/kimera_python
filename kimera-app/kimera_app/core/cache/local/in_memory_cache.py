from kimera_core.components.storage.dynamic.cache.local.engines import InMemoryCacheEngine

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
