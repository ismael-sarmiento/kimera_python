"""
    The pickle module implements binary protocols for serializing and de-serializing a Python object structure
    Documentation: https://docs.python.org/3/library/pickle.html
"""

import pickle
from datetime import datetime


class Pickle:

    @staticmethod
    def serializer(_object: object) -> bytes:
        return pickle.dumps(_object)

    @staticmethod
    def deserializer(serializer_object: bytes) -> object:
        return pickle.loads(serializer_object)


if __name__ == '__main__':
    # -------------------------------------------------------------------
    # ------------------------- EXAMPLES --------------------------------
    # -------------------------------------------------------------------

    a = 1
    b = "'1'"
    c = 1.0
    d = [a, b, c]
    e = {'a': a, 'b': b, 'c': c, 'd': d}
    f = (2, 3)
    g = datetime.now()
    h = {'1': g, '2': f, '3': d, '4': g.date()}
    i = [a, b, c, d, e, f, g, datetime.now().date(), [g.date(), g.date()]]
    j = [Pickle]

    # ----------------------- KIMERA SERIALIZER --------------------------
    print(f'\n\t PICKLE')
    for obj, count in zip(j, range(len(j))):
        print(f'\nIterator {count}')
        print(f'\tObject {obj} with type {type(obj)}')
        serialize_object = Pickle.serializer(obj)
        print(f'\tSerialize object {serialize_object} with type {type(serialize_object)}')
        deserialize_object = Pickle.deserializer(serialize_object)
        print(f'\tDeserialize object {deserialize_object} with type {type(deserialize_object)}')
        print(f'Result: {obj == deserialize_object}')
