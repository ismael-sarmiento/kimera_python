import unittest
from datetime import datetime
from time import time

from kimera_core.components.tools.serializers import custom


class A:

    def __init__(self, state):
        self.state = state


class TestToolsSerializersCustom(unittest.TestCase):

    def setUp(self) -> None:
        self.kimera_serializer = custom()

    def tearDown(self) -> None:
        print(self.shortDescription())

    def test_given_object_type_str_when_serializer_and_deserializer_then_return_same_object(self):
        self._testMethodDoc = "I - test_given_object_type_str_when_serializer_and_deserializer_then_return_same_object"

        expected_object = "1"

        serializer_object = self.kimera_serializer.serialize(expected_object)
        deserializer_object = self.kimera_serializer.deserialize(serializer_object)
        self.assertEqual(deserializer_object, expected_object)

    def test_given_object_type_int_when_serializer_and_deserializer_then_return_same_object(self):
        self._testMethodDoc = "II - test_given_object_type_int_when_serializer_and_deserializer_then_return_same_object"

        expected_object = 1

        serializer_object = self.kimera_serializer.serialize(expected_object)
        deserializer_object = self.kimera_serializer.deserialize(serializer_object)
        self.assertEqual(deserializer_object, expected_object)

    def test_given_object_type_list_when_serializer_and_deserializer_then_return_same_object(self):
        self._testMethodDoc = "III - test_given_object_type_list_when_serializer_and_deserializer_then_return_same_object"

        expected_object = [1, "1"]

        serializer_object = self.kimera_serializer.serialize(expected_object)
        deserializer_object = self.kimera_serializer.deserialize(serializer_object)
        self.assertEqual(deserializer_object, expected_object)

    def test_given_object_type_tuple_when_serializer_and_deserializer_then_return_same_object(self):
        self._testMethodDoc = "IV - test_given_object_type_tuple_when_serializer_and_deserializer_then_return_same_object"

        expected_object = (1, "1")

        serializer_object = self.kimera_serializer.serialize(expected_object)
        deserializer_object = self.kimera_serializer.deserialize(serializer_object)
        self.assertEqual(deserializer_object, expected_object)

    def test_given_object_type_dict_when_serializer_and_deserializer_then_return_same_object(self):
        self._testMethodDoc = "V - test_given_object_type_dict_when_serializer_and_deserializer_then_return_same_object"

        expected_object = {"A": 1, "B": ["1", 2, (8, 32)]}

        serializer_object = self.kimera_serializer.serialize(expected_object)
        deserializer_object = self.kimera_serializer.deserialize(serializer_object)
        self.assertEqual(deserializer_object, expected_object)

    def test_given_advancedI_object_when_serializer_and_deserializer_then_return_same_object(self):
        self._testMethodDoc = "VI - test_given_advancedI_object_when_serializer_and_deserializer_then_return_same_object"

        expected_object = {"A": [1, datetime.now(), datetime.now().date()], "B": ["1", 2, (8, 32)]}

        serializer_object = self.kimera_serializer.serialize(expected_object)
        deserializer_object = self.kimera_serializer.deserialize(serializer_object)
        self.assertEqual(deserializer_object, expected_object)

    def test_given_advancedII_object_when_serializer_and_deserializer_then_return_same_object(self):
        self._testMethodDoc = "VII - test_given_advancedII_object_when_serializer_and_deserializer_then_return_same_object"

        expected_object = {"A": [1, datetime.now(), datetime.now().date(), time().__doc__, time()], "B": ["1", 2, (8, 32)]}

        serializer_object = self.kimera_serializer.serialize(expected_object)
        deserializer_object = self.kimera_serializer.deserialize(serializer_object)
        self.assertEqual(deserializer_object, expected_object)

    def test_given_not_singleton_class_when_serializer_and_deserializer_then_return_different_object(self):
        self._testMethodDoc = "VIII - test_given_advanced_object_when_serializer_and_deserializer_then_return_same_object"

        expected_object = A(1)

        with self.assertRaises(TypeError):
            self.kimera_serializer.serialize(expected_object)
