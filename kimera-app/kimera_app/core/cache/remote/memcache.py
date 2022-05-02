from kimera_core.components.storage.dynamic.cache.remote.engines import MemcachedEngine

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
