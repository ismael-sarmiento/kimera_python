import unittest

from kimera_core.components.tools.hash.md5 import build_hash


class A:

    def __init__(self, state):
        self.state = state


class TestToolsHashMD5(unittest.TestCase):

    def tearDown(self) -> None:
        print(self.shortDescription())

    def test_given_object_type_str_when_call_build_hash_any_times_then_return_same_value(self):
        self._testMethodDoc = "I - test_given_object_type_str_when_call_build_hash_any_times_then_return_same_value"

        obj = "1"

        hash1 = build_hash(obj)
        hash2 = build_hash(obj)
        self.assertEqual(hash1, hash2)

    def test_given_object_type_int_when_call_build_hash_any_times_then_return_same_value(self):
        self._testMethodDoc = "II - test_given_object_type_int_when_call_build_hash_any_times_then_return_same_value"

        obj = 1

        hash1 = build_hash(obj)
        hash2 = build_hash(obj)
        self.assertEqual(hash1, hash2)

    def test_given_object_type_list_when_call_build_hash_any_times_then_return_same_value(self):
        self._testMethodDoc = "III - test_given_object_type_list_when_call_build_hash_any_times_then_return_same_value"

        obj = [1, "1"]

        hash1 = build_hash(obj)
        hash2 = build_hash(obj)
        self.assertEqual(hash1, hash2)

    def test_given_object_type_tuple_when_call_build_hash_any_times_then_return_same_value(self):
        self._testMethodDoc = "IV - test_given_object_type_tuple_when_call_build_hash_any_times_then_return_same_value"

        obj = (1, "1")

        hash1 = build_hash(obj)
        hash2 = build_hash(obj)
        self.assertEqual(hash1, hash2)

    def test_given_object_type_dict_when_call_build_hash_any_times_then_return_same_value(self):
        self._testMethodDoc = "V - test_given_object_type_dict_when_call_build_hash_any_times_then_return_same_value"

        obj = {"A": 1, "B": "1"}

        hash1 = build_hash(obj)
        hash2 = build_hash(obj)
        self.assertEqual(hash1, hash2)

    def test_given_object_type_class_when_call_build_hash_any_times_then_return_same_value(self):
        self._testMethodDoc = "VI - test_given_object_type_class_when_call_build_hash_any_times_then_return_same_value"

        obj = A("1")

        hash1 = build_hash(obj)
        hash2 = build_hash(obj)
        self.assertEqual(hash1, hash2)
