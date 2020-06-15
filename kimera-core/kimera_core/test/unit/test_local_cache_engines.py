import unittest
from time import sleep

from kimera_core.components.storage.dynamic.cache.local.engines import InMemoryCacheEngine, BaseCacheEngine, LocalCacheEngine, ThreadCacheEngine, \
    thread_local_cache, in_memory_local_cache


@in_memory_local_cache("key4")
def my_function_a(value):
    return value


@thread_local_cache("key4")
def my_function_b(value):
    return value


class TestLocalCacheEngine(unittest.TestCase):

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
        print(self.shortDescription())

    # -------------------------------------------------------------------
    # IN MEMORY LOCAL CACHE
    # -------------------------------------------------------------------
    def test_given_set_key_pair_value_when_store_in_memory_local_cache_then_exists_all_set(self):
        self._testMethodDoc = "I - test_given_set_key_pair_value_when_store_in_memory_local_cache_then_exists_all_set"

        self.in_memory_cache.set(self.pairI["key"], self.pairI["value"])
        self.in_memory_cache.set(self.pairII["key"], self.pairII["value"])
        self.in_memory_cache.set(self.pairIII["key"], self.pairIII["value"])

        self.assertTrue(self.in_memory_cache.exists(self.pairI["key"]))
        self.assertTrue(self.in_memory_cache.exists(self.pairII["key"]))
        self.assertTrue(self.in_memory_cache.exists(self.pairIII["key"]))

    def test_given_set_key_pair_value_when_store_in_memory_local_cache_then_recovery_all_set(self):
        self._testMethodDoc = "II - test_given_set_key_pair_value_when_store_in_memory_local_cache_then_recovery_all_set"

        self.in_memory_cache.set(self.pairI["key"], self.pairI["value"])
        self.in_memory_cache.set(self.pairII["key"], self.pairII["value"])
        self.in_memory_cache.set(self.pairIII["key"], self.pairIII["value"])

        self.assertEqual(self.in_memory_cache.get(self.pairI["key"]), "valueI")
        self.assertEqual(self.in_memory_cache.get(self.pairII["key"]), "valueII")
        self.assertEqual(self.in_memory_cache.get(self.pairIII["key"]), "valueIII")

    def test_given_set_key_pair_value_when_store_in_memory_local_cache_and_delete_a_set_then_recovery_all_set(self):
        self._testMethodDoc = "III - test_given_set_key_pair_value_when_store_in_memory_local_cache_and_delete_a_set_then_recovery_all_set"

        self.in_memory_cache.set(self.pairI["key"], self.pairI["value"])
        self.in_memory_cache.set(self.pairII["key"], self.pairII["value"])
        self.in_memory_cache.set(self.pairIII["key"], self.pairIII["value"])
        self.in_memory_cache.delete(self.pairIII["key"])

        self.assertEqual(self.in_memory_cache.get(self.pairI["key"]), "valueI")
        self.assertEqual(self.in_memory_cache.get(self.pairII["key"]), "valueII")

    def test_given_set_key_pair_value_when_store_in_memory_local_cache_and_clear_cache_then_not_exists_all_set(self):
        self._testMethodDoc = "IV - test_given_set_key_pair_value_when_store_in_memory_local_cache_and_clear_cache_then_not_exists_all_set"

        self.in_memory_cache.set(self.pairI["key"], self.pairI["value"])
        self.in_memory_cache.set(self.pairII["key"], self.pairII["value"])
        self.in_memory_cache.set(self.pairIII["key"], self.pairIII["value"])
        self.in_memory_cache.clear()

        self.assertFalse(self.in_memory_cache.exists(self.pairI["key"]))
        self.assertFalse(self.in_memory_cache.exists(self.pairII["key"]))
        self.assertFalse(self.in_memory_cache.exists(self.pairIII["key"]))

    def test_given_set_key_pair_value_when_store_in_memory_local_cache_and_set_max_size_then_remove_last_key_pair_value(self):
        self._testMethodDoc = "V - test_given_set_key_pair_value_when_store_in_memory_local_cache_and_set_max_size_" \
                              "then_remove_last_key_pair_value"

        self.in_memory_cache.set(self.pairI["key"], self.pairI["value"])
        self.in_memory_cache.set(self.pairII["key"], self.pairII["value"])
        self.in_memory_cache.set(self.pairIII["key"], self.pairIII["value"], size=1)

        self.assertTrue(self.in_memory_cache.exists(self.pairI["key"]))
        self.assertFalse(self.in_memory_cache.exists(self.pairII["key"]))
        self.assertTrue(self.in_memory_cache.exists(self.pairIII["key"]))

    def test_given_set_key_pair_value_when_store_in_memory_local_cache_and_set_timeout_then_remove_key_pair_value_after_scheduled_time(self):
        self._testMethodDoc = "VI - test_given_set_key_pair_value_when_store_in_memory_local_cache_and_set_timeout_then_" \
                              "remove_key_pair_value_after_scheduled_time"

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

    def test_given_set_key_pair_value_when_store_in_memory_local_cache_and_set_size_and_timeout_then_process_is_validated(self):
        self._testMethodDoc = "VII - test_given_set_key_pair_value_when_store_in_memory_local_cache_and_set_size_and_timeout_" \
                              "then_process_is_validated"

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
        self._testMethodDoc = "VIII - test_given_set_key_pair_value_when_store_in_thread_local_cache_then_exists_all_set"

        self.thread_local_cache.set(self.pairI["key"], self.pairI["value"])
        self.thread_local_cache.set(self.pairII["key"], self.pairII["value"])
        self.thread_local_cache.set(self.pairIII["key"], self.pairIII["value"])

        self.assertTrue(self.thread_local_cache.exists(self.pairI["key"]))
        self.assertTrue(self.thread_local_cache.exists(self.pairII["key"]))
        self.assertTrue(self.thread_local_cache.exists(self.pairIII["key"]))

    def test_given_set_key_pair_value_when_store_in_thread_local_cache_then_recovery_all_set(self):
        self._testMethodDoc = "II - test_given_set_key_pair_value_when_store_in_thread_local_cache_then_recovery_all_set"

        self.thread_local_cache.set(self.pairI["key"], self.pairI["value"])
        self.thread_local_cache.set(self.pairII["key"], self.pairII["value"])
        self.thread_local_cache.set(self.pairIII["key"], self.pairIII["value"])

        self.assertEqual(self.thread_local_cache.get(self.pairI["key"]), "valueI")
        self.assertEqual(self.thread_local_cache.get(self.pairII["key"]), "valueII")
        self.assertEqual(self.thread_local_cache.get(self.pairIII["key"]), "valueIII")

    def test_given_set_key_pair_value_when_store_in_thread_local_cache_and_delete_a_set_then_recovery_all_set(self):
        self._testMethodDoc = "IX - test_given_set_key_pair_value_when_store_in_thread_local_cache_and_delete_a_set_then_recovery_all_set"

        self.thread_local_cache.set(self.pairI["key"], self.pairI["value"])
        self.thread_local_cache.set(self.pairII["key"], self.pairII["value"])
        self.thread_local_cache.set(self.pairIII["key"], self.pairIII["value"])
        self.thread_local_cache.delete(self.pairIII["key"])

        self.assertEqual(self.thread_local_cache.get(self.pairI["key"]), "valueI")
        self.assertEqual(self.thread_local_cache.get(self.pairII["key"]), "valueII")

    def test_given_set_key_pair_value_when_store_in_thread_local_cache_and_clear_cache_then_not_exists_all_set(self):
        self._testMethodDoc = "X - test_given_set_key_pair_value_when_store_in_thread_local_cache_and_clear_cache_then_not_exists_all_set"

        self.thread_local_cache.set(self.pairI["key"], self.pairI["value"])
        self.thread_local_cache.set(self.pairII["key"], self.pairII["value"])
        self.thread_local_cache.set(self.pairIII["key"], self.pairIII["value"])
        self.thread_local_cache.clear()

        self.assertFalse(self.thread_local_cache.exists(self.pairI["key"]))
        self.assertFalse(self.thread_local_cache.exists(self.pairII["key"]))
        self.assertFalse(self.thread_local_cache.exists(self.pairIII["key"]))

    def test_given_set_key_pair_value_when_store_in_thread_local_cache_and_set_max_size_then_remove_last_key_pair_value(self):
        self._testMethodDoc = "XI - test_given_set_key_pair_value_when_store_in_thread_local_cache_and_set_max_size_" \
                              "then_remove_last_key_pair_value"

        self.thread_local_cache.set(self.pairI["key"], self.pairI["value"])
        self.thread_local_cache.set(self.pairII["key"], self.pairII["value"])
        self.thread_local_cache.set(self.pairIII["key"], self.pairIII["value"], size=1)

        self.assertTrue(self.thread_local_cache.exists(self.pairI["key"]))
        self.assertFalse(self.thread_local_cache.exists(self.pairII["key"]))
        self.assertTrue(self.thread_local_cache.exists(self.pairIII["key"]))

    def test_given_set_key_pair_value_when_store_in_thread_local_cache_and_set_timeout_then_remove_key_pair_value_after_scheduled_time(self):
        self._testMethodDoc = "XII - test_given_set_key_pair_value_when_store_in_thread_local_cache_and_set_timeout_" \
                              "then_remove_key_pair_value_after_scheduled_time"

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

    def test_given_set_key_pair_value_when_store_in_thread_local_cache_and_set_size_and_timeout_then_process_is_validated(self):
        self._testMethodDoc = "XIII - test_given_set_key_pair_value_when_store_in_thread_local_cache_and_set_size_and_timeout_" \
                              "then_process_is_validated"

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
    def test_given_function_with_return_when_store_in_memory_local_cache_by_decorator_and_set_size_and_timeout_then_process_is_validated(self):
        self._testMethodDoc = "XIV - test_given_function_with_return_when_store_in_memory_local_cache_by_decorator_and_set_size_and_timeout_" \
                              "then_process_is_validated"

        expected_value = my_function_a("valueIV")

        self.assertTrue(self.in_memory_cache.exists("key4"))
        self.assertTrue(self.in_memory_cache.get("key4"), expected_value)

    def test_given_function_with_return_when_store_in_thread_local_cache_by_decorator_and_set_size_and_timeout_then_process_is_validated(self):
        self._testMethodDoc = "XV - test_given_function_with_return_when_store_in_thread_local_cache_by_decorator_and_set_size_and_timeout_" \
                              "then_process_is_validated"

        expected_value = my_function_b("valueIV")

        self.assertTrue(self.thread_local_cache.exists("key4"))
        self.assertTrue(self.thread_local_cache.get("key4"), expected_value)

    def test_should_check_class_inheritance(self):
        self._testMethodDoc = "XVI - test_should_check_class_inheritance"

        self.assertTrue(issubclass(self.in_memory_cache.__class__, self.base_cache_engine.__class__))
        self.assertTrue(issubclass(self.thread_local_cache.__class__, self.base_cache_engine.__class__))
        self.assertTrue(issubclass(self.in_memory_cache.__class__, self.local_cache_engine.__class__))
        self.assertTrue(issubclass(self.thread_local_cache.__class__, self.local_cache_engine.__class__))
