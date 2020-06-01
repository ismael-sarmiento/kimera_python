""" This module contains different implementations to get the hash of an object """

import hashlib


def build_hash(_obj: object) -> str:
    """
    Method that build a unique and unrepeatable key to the state of an object
    :param _obj: Input object.
    :return: [String] Unique key (hash) of the object
    """
    return hashlib.md5(str(_obj).encode() + str(type(_obj)).encode()).hexdigest()


if __name__ == '__main__':
    # -------------------------------------------------------------------
    # ------------------------- EXAMPLES --------------------------------
    # -------------------------------------------------------------------

    class A:

        def __init__(self, state):
            self.state = state


    a = '1'
    b = "1"
    k = 1
    r = 1.0
    c = [a, b]
    d = {'a': a, 'b': b, 'c': c, 'd': (a, b)}
    e = A(1)
    f = A(2)
    g = [e, f]
    i = [e, f]
    h = [a, b, c, d, e, f, g, i, k, r]

    for obj in h:
        print(f"\nObject: {obj} type: {type(obj)}")
        hash1 = build_hash(obj)
        print(f"\t Hash1: {hash1}")
        hash2 = build_hash(obj)
        print(f"\t Hash2: {hash2}")
        print(f"\t Result: {hash1 == hash2}")
