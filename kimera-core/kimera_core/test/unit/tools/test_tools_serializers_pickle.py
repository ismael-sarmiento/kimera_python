import unittest
from datetime import datetime
from time import time

from kimera_core.components.tools.serializers import pickle


class A:

    def __init__(self, state):
        self.state = state


class TestToolsSerializersPickle(unittest.TestCase):

    def setUp(self) -> None:
        self.pickle = pickle()

    def tearDown(self) -> None:
        print(self.id())

    def test_given_object_type_str_when_serializer_and_deserializer_then_return_same_object(self):
        expected_object = "1"

        serializer_object = self.pickle.serializer(expected_object)
        deserializer_object = self.pickle.deserializer(serializer_object)
        self.assertEqual(deserializer_object, expected_object)

    def test_given_object_type_int_when_serializer_and_deserializer_then_return_same_object(self):
        expected_object = 1

        serializer_object = self.pickle.serializer(expected_object)
        deserializer_object = self.pickle.deserializer(serializer_object)
        self.assertEqual(deserializer_object, expected_object)

    def test_given_object_type_list_when_serializer_and_deserializer_then_return_same_object(self):
        expected_object = [1, "1"]

        serializer_object = self.pickle.serializer(expected_object)
        deserializer_object = self.pickle.deserializer(serializer_object)
        self.assertEqual(deserializer_object, expected_object)

    def test_given_object_type_tuple_when_serializer_and_deserializer_then_return_same_object(self):
        expected_object = (1, "1")

        serializer_object = self.pickle.serializer(expected_object)
        deserializer_object = self.pickle.deserializer(serializer_object)
        self.assertEqual(deserializer_object, expected_object)

    def test_given_object_type_dict_when_serializer_and_deserializer_then_return_same_object(self):
        expected_object = {"A": 1, "B": ["1", 2, (8, 32)]}

        serializer_object = self.pickle.serializer(expected_object)
        deserializer_object = self.pickle.deserializer(serializer_object)
        self.assertEqual(deserializer_object, expected_object)

    def test_given_advanced_object_when_serializer_and_deserializer_then_return_same_object(self):
        expected_object = {"A": [1, A, datetime.now(), datetime.now().date()], "B": ["1", 2, (8, 32), time()]}

        serializer_object = self.pickle.serializer(expected_object)
        deserializer_object = self.pickle.deserializer(serializer_object)
        self.assertEqual(deserializer_object, expected_object)

    def test_given_not_singleton_class_when_serializer_and_deserializer_then_return_different_object(self):
        expected_object = A(3)

        serializer_object = self.pickle.serializer(expected_object)
        deserializer_object = self.pickle.deserializer(serializer_object)
        self.assertFalse(deserializer_object == expected_object)
