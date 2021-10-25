import unittest
from time import sleep

from kimera_core.components.storage.dynamic.cache.local.engines import InMemoryCacheEngine, BaseCacheEngine, \
    LocalCacheEngine, ThreadCacheEngine, \
    thread_local_cache, in_memory_local_cache


@in_memory_local_cache("key4")
def my_function_a(value):
    return value


@thread_local_cache("key4")
def my_function_b(value):
    return value


class TestDynamicCacheLocalEngines(unittest.TestCase):

    def setUp(self) -> None:
        self.in_memory_cache = InMemoryCacheEngine()
        self.thread_local_cache = ThreadCacheEngine()
        BaseCacheEngine.__abstractmethods__ = set()
        self.base_cache_engine = BaseCacheEngine()
        LocalCacheEngine.__abstractmethods__ = set()
        self.local_cache_engine = LocalCacheEngine()
        self.pairI = {"key": "keyI", "value": "valueI"}
        self.pairII = {"key": "keyII", "value": "valueII"}
        self.pairIII = {"key": "keyIII", "value": "valueIII"}

    def tearDown(self) -> None:
        self._testMethodDoc = f"{self.__dict__['_testMethodName']}"
        print(self.shortDescription())

    # -------------------------------------------------------------------
    # IN MEMORY LOCAL CACHE
    # -------------------------------------------------------------------
    def test_given_set_key_pair_value_when_store_in_memory_local_cache_then_exists_all_set(self):
        self.in_memory_cache.set(self.pairI["key"], self.pairI["value"])
        self.in_memory_cache.set(self.pairII["key"], self.pairII["value"])
        self.in_memory_cache.set(self.pairIII["key"], self.pairIII["value"])

        self.assertTrue(self.in_memory_cache.exists(self.pairI["key"]))
        self.assertTrue(self.in_memory_cache.exists(self.pairII["key"]))
        self.assertTrue(self.in_memory_cache.exists(self.pairIII["key"]))

    def test_given_set_key_pair_value_when_store_in_memory_local_cache_then_recovery_all_set(self):
        self.in_memory_cache.set(self.pairI["key"], self.pairI["value"])
        self.in_memory_cache.set(self.pairII["key"], self.pairII["value"])
        self.in_memory_cache.set(self.pairIII["key"], self.pairIII["value"])

        self.assertEqual(self.in_memory_cache.get(self.pairI["key"]), "valueI")
        self.assertEqual(self.in_memory_cache.get(self.pairII["key"]), "valueII")
        self.assertEqual(self.in_memory_cache.get(self.pairIII["key"]), "valueIII")

    def test_given_set_key_pair_value_when_store_in_memory_local_cache_and_delete_a_set_then_recovery_all_set(self):
        self.in_memory_cache.set(self.pairI["key"], self.pairI["value"])
        self.in_memory_cache.set(self.pairII["key"], self.pairII["value"])
        self.in_memory_cache.set(self.pairIII["key"], self.pairIII["value"])
        self.in_memory_cache.delete(self.pairIII["key"])

        self.assertEqual(self.in_memory_cache.get(self.pairI["key"]), "valueI")
        self.assertEqual(self.in_memory_cache.get(self.pairII["key"]), "valueII")

    def test_given_set_key_pair_value_when_store_in_memory_local_cache_and_clear_cache_then_not_exists_all_set(self):
        self.in_memory_cache.set(self.pairI["key"], self.pairI["value"])
        self.in_memory_cache.set(self.pairII["key"], self.pairII["value"])
        self.in_memory_cache.set(self.pairIII["key"], self.pairIII["value"])
        self.in_memory_cache.clear()

        self.assertFalse(self.in_memory_cache.exists(self.pairI["key"]))
        self.assertFalse(self.in_memory_cache.exists(self.pairII["key"]))
        self.assertFalse(self.in_memory_cache.exists(self.pairIII["key"]))

    def test_given_set_key_pair_value_when_store_in_memory_local_cache_and_set_max_size_then_remove_last_key_pair_value(
            self):
        self.in_memory_cache.set(self.pairI["key"], self.pairI["value"])
        self.in_memory_cache.set(self.pairII["key"], self.pairII["value"])
        self.in_memory_cache.set(self.pairIII["key"], self.pairIII["value"], size=1)

        self.assertTrue(self.in_memory_cache.exists(self.pairI["key"]))
        self.assertFalse(self.in_memory_cache.exists(self.pairII["key"]))
        self.assertTrue(self.in_memory_cache.exists(self.pairIII["key"]))

    def test_given_set_key_pair_value_when_store_in_memory_local_cache_and_set_timeout_then_remove_key_pair_value_after_scheduled_time(
            self):
        self.in_memory_cache.set(self.pairI["key"], self.pairI["value"], timeout=0.5)
        self.in_memory_cache.set(self.pairII["key"], self.pairII["value"])
        self.in_memory_cache.set(self.pairIII["key"], self.pairIII["value"], timeout=1)

        sleep(1)

        self.assertFalse(self.in_memory_cache.exists(self.pairI["key"]))
        self.assertFalse(self.in_memory_cache.get(self.pairI["key"]))
        self.assertTrue(self.in_memory_cache.exists(self.pairII["key"]))
        self.assertEqual(self.in_memory_cache.get(self.pairII["key"]), "valueII")
        self.assertFalse(self.in_memory_cache.exists(self.pairIII["key"]))
        self.assertFalse(self.in_memory_cache.get(self.pairIII["key"]))

    def test_given_set_key_pair_value_when_store_in_memory_local_cache_and_set_size_and_timeout_then_process_is_validated(
            self):
        self.in_memory_cache.set(self.pairI["key"], self.pairI["value"], timeout=3)
        self.in_memory_cache.set(self.pairII["key"], self.pairII["value"], timeout=2, size=1)
        self.in_memory_cache.set(self.pairIII["key"], self.pairIII["value"], timeout=1, size=1)

        sleep(1)

        self.assertTrue(self.in_memory_cache.exists(self.pairI["key"]))
        self.assertEqual(self.in_memory_cache.get(self.pairI["key"]), "valueI")
        self.assertFalse(self.in_memory_cache.exists(self.pairII["key"]))
        self.assertEqual(self.in_memory_cache.get(self.pairII["key"]), None)
        self.assertFalse(self.in_memory_cache.exists(self.pairIII["key"]))
        self.assertEqual(self.in_memory_cache.get(self.pairIII["key"]), None)

    # -------------------------------------------------------------------
    # THREAD LOCAL CACHE
    # -------------------------------------------------------------------
    def test_given_set_key_pair_value_when_store_in_thread_local_cache_then_exists_all_set(self):
        self.thread_local_cache.set(self.pairI["key"], self.pairI["value"])
        self.thread_local_cache.set(self.pairII["key"], self.pairII["value"])
        self.thread_local_cache.set(self.pairIII["key"], self.pairIII["value"])

        self.assertTrue(self.thread_local_cache.exists(self.pairI["key"]))
        self.assertTrue(self.thread_local_cache.exists(self.pairII["key"]))
        self.assertTrue(self.thread_local_cache.exists(self.pairIII["key"]))

    def test_given_set_key_pair_value_when_store_in_thread_local_cache_then_recovery_all_set(self):
        self.thread_local_cache.set(self.pairI["key"], self.pairI["value"])
        self.thread_local_cache.set(self.pairII["key"], self.pairII["value"])
        self.thread_local_cache.set(self.pairIII["key"], self.pairIII["value"])

        self.assertEqual(self.thread_local_cache.get(self.pairI["key"]), "valueI")
        self.assertEqual(self.thread_local_cache.get(self.pairII["key"]), "valueII")
        self.assertEqual(self.thread_local_cache.get(self.pairIII["key"]), "valueIII")

    def test_given_set_key_pair_value_when_store_in_thread_local_cache_and_delete_a_set_then_recovery_all_set(self):
        self.thread_local_cache.set(self.pairI["key"], self.pairI["value"])
        self.thread_local_cache.set(self.pairII["key"], self.pairII["value"])
        self.thread_local_cache.set(self.pairIII["key"], self.pairIII["value"])
        self.thread_local_cache.delete(self.pairIII["key"])

        self.assertEqual(self.thread_local_cache.get(self.pairI["key"]), "valueI")
        self.assertEqual(self.thread_local_cache.get(self.pairII["key"]), "valueII")

    def test_given_set_key_pair_value_when_store_in_thread_local_cache_and_clear_cache_then_not_exists_all_set(self):
        self.thread_local_cache.set(self.pairI["key"], self.pairI["value"])
        self.thread_local_cache.set(self.pairII["key"], self.pairII["value"])
        self.thread_local_cache.set(self.pairIII["key"], self.pairIII["value"])
        self.thread_local_cache.clear()

        self.assertFalse(self.thread_local_cache.exists(self.pairI["key"]))
        self.assertFalse(self.thread_local_cache.exists(self.pairII["key"]))
        self.assertFalse(self.thread_local_cache.exists(self.pairIII["key"]))

    def test_given_set_key_pair_value_when_store_in_thread_local_cache_and_set_max_size_then_remove_last_key_pair_value(
            self):
        self.thread_local_cache.set(self.pairI["key"], self.pairI["value"])
        self.thread_local_cache.set(self.pairII["key"], self.pairII["value"])
        self.thread_local_cache.set(self.pairIII["key"], self.pairIII["value"], size=1)

        self.assertTrue(self.thread_local_cache.exists(self.pairI["key"]))
        self.assertFalse(self.thread_local_cache.exists(self.pairII["key"]))
        self.assertTrue(self.thread_local_cache.exists(self.pairIII["key"]))

    def test_given_set_key_pair_value_when_store_in_thread_local_cache_and_set_timeout_then_remove_key_pair_value_after_scheduled_time(
            self):
        self.thread_local_cache.set(self.pairI["key"], self.pairI["value"], timeout=0.5)
        self.thread_local_cache.set(self.pairII["key"], self.pairII["value"])
        self.thread_local_cache.set(self.pairIII["key"], self.pairIII["value"], timeout=1)

        sleep(1)

        self.assertFalse(self.thread_local_cache.exists(self.pairI["key"]))
        self.assertFalse(self.thread_local_cache.get(self.pairI["key"]))
        self.assertTrue(self.thread_local_cache.exists(self.pairII["key"]))
        self.assertEqual(self.thread_local_cache.get(self.pairII["key"]), "valueII")
        self.assertFalse(self.thread_local_cache.exists(self.pairIII["key"]))
        self.assertFalse(self.thread_local_cache.get(self.pairIII["key"]))

    def test_given_set_key_pair_value_when_store_in_thread_local_cache_and_set_size_and_timeout_then_process_is_validated(
            self):
        self.thread_local_cache.set(self.pairI["key"], self.pairI["value"], timeout=3)
        self.thread_local_cache.set(self.pairII["key"], self.pairII["value"], timeout=2, size=1)
        self.thread_local_cache.set(self.pairIII["key"], self.pairIII["value"], timeout=1, size=1)

        sleep(1)

        self.assertTrue(self.thread_local_cache.exists(self.pairI["key"]))
        self.assertEqual(self.thread_local_cache.get(self.pairI["key"]), "valueI")
        self.assertFalse(self.thread_local_cache.exists(self.pairII["key"]))
        self.assertEqual(self.thread_local_cache.get(self.pairII["key"]), None)
        self.assertFalse(self.thread_local_cache.exists(self.pairIII["key"]))
        self.assertEqual(self.thread_local_cache.get(self.pairIII["key"]), None)

    # -------------------------------------------------------------------
    # DECORATORS
    # -------------------------------------------------------------------
    def test_given_function_with_return_when_store_in_memory_local_cache_by_decorator_and_set_size_and_timeout_then_process_is_validated(
            self):
        expected_value = my_function_a("valueIV")

        self.assertTrue(self.in_memory_cache.exists("key4"))
        self.assertTrue(self.in_memory_cache.get("key4"), expected_value)

    def test_given_function_with_return_when_store_in_thread_local_cache_by_decorator_and_set_size_and_timeout_then_process_is_validated(
            self):
        expected_value = my_function_b("valueIV")

        self.assertTrue(self.thread_local_cache.exists("key4"))
        self.assertTrue(self.thread_local_cache.get("key4"), expected_value)

    # -------------------------------------------------------------------
    # INHERITANCE
    # -------------------------------------------------------------------
    def test_should_check_class_inheritance(self):
        self.assertTrue(issubclass(self.in_memory_cache.__class__, self.base_cache_engine.__class__))
        self.assertTrue(issubclass(self.thread_local_cache.__class__, self.base_cache_engine.__class__))
        self.assertTrue(issubclass(self.in_memory_cache.__class__, self.local_cache_engine.__class__))
        self.assertTrue(issubclass(self.thread_local_cache.__class__, self.local_cache_engine.__class__))
