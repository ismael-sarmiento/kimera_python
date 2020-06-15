from datetime import datetime

from kimera_core.components.tools.serializers._pickle import Pickle
from kimera_core.components.tools.serializers.custom import KimeraSerializer

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

    # ----------------------- PICKLE SERIALIZER --------------------------
    print(f'\n\t PICKLE')
    for obj, count in zip(j, range(len(j))):
        print(f'\nIterator {count}')
        print(f'\tObject {obj} with type {type(obj)}')
        serialize_object = Pickle.serializer(obj)
        print(f'\tSerialize object {serialize_object} with type {type(serialize_object)}')
        deserialize_object = Pickle.deserializer(serialize_object)
        print(f'\tDeserialize object {deserialize_object} with type {type(deserialize_object)}')
        print(f'Result: {obj == deserialize_object}')

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

    # ----------------------- KIMERA SERIALIZER --------------------------
    print(f'\n\t KIMERA SERIALIZER')
    for obj, count in zip(i, range(len(i))):
        print(f'\nIterator {count}')
        print(f'\tObject {obj} with type {type(obj)}')
        serialize_object = KimeraSerializer().serialize(obj)
        print(f'\tSerialize object {serialize_object} with type {type(serialize_object)}')
        deserialize_object = KimeraSerializer().deserialize(serialize_object)
        print(f'\tDeserialize object {deserialize_object} with type {type(deserialize_object)}')
        print(f'Result: {obj == deserialize_object}')
