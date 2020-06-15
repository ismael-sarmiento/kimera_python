"""
    The pickle module implements binary protocols for serializing and de-serializing a Python object structure
    Documentation: https://docs.python.org/3/library/pickle.html
"""

import pickle


class Pickle:

    @staticmethod
    def serializer(_object: object) -> bytes:
        return pickle.dumps(_object)

    @staticmethod
    def deserializer(serializer_object: bytes) -> object:
        return pickle.loads(serializer_object)