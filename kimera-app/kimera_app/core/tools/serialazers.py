from datetime import datetime

from kimera_core.components.tools.serializers import pickle, custom

if __name__ == '__main__':
    # -------------------------------------------------------------------
    # ------------------------- EXAMPLES --------------------------------
    # -------------------------------------------------------------------

    # ----------------------- PICKLE SERIALIZER --------------------------

    a = 1
    b = "'1'"
    c = 1.0
    d = [a, b, c]
    e = {'a': a, 'b': b, 'c': c, 'd': d}
    f = (2, 3)
    g = datetime.now()
    h = {'1': g, '2': f, '3': d, '4': g.date()}
    i = [a, b, c, d, e, f, g, datetime.now().date(), [g.date(), g.date()]]
    j = [pickle()]

    print(f'\n\t PICKLE')
    for obj, count in zip(j, range(len(j))):
        print(f'\nIterator {count}')
        print(f'\tObject {obj} with type {type(obj)}')
        serialize_object = pickle().serializer(obj)
        print(f'\tSerialize object {serialize_object} with type {type(serialize_object)}')
        deserialize_object = pickle().deserializer(serialize_object)
        print(f'\tDeserialize object {deserialize_object} with type {type(deserialize_object)}')
        print(f'Result: {obj == deserialize_object}')

    # ----------------------- KIMERA SERIALIZER --------------------------

    a = 1
    b = "'1'"
    c = 1.0
    d = [a, b, c]
    e = {'a': a, 'b': b, 'c': c, 'd': d}
    f = (2, 3)
    g = datetime.now()
    h = {'1': g, '2': f, '3': d, '4': g.date()}
    i = [a, b, c, d, e, f, g, datetime.now().date(), [g.date(), g.date()]]

    print(f'\n\t KIMERA SERIALIZER')
    for obj, count in zip(i, range(len(i))):
        print(f'\nIterator {count}')
        print(f'\tObject {obj} with type {type(obj)}')
        serialize_object = custom().serialize(obj)
        print(f'\tSerialize object {serialize_object} with type {type(serialize_object)}')
        deserialize_object = custom().deserialize(serialize_object)
        print(f'\tDeserialize object {deserialize_object} with type {type(deserialize_object)}')
        print(f'Result: {obj == deserialize_object}')
