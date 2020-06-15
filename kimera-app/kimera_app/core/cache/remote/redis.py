from kimera_core.components.storage.dynamic.cache.remote.engines import RedisEngine

if __name__ == '__main__':
    # -------------------------------------------------------------------
    # ------------------------- EXAMPLES --------------------------------
    # -------------------------------------------------------------------
    # TODO: falta añadir un memcache real y los test
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
