""" This module contains different implementations to get the hash of an object """

import hashlib


def _md5(_object: object) -> str:
    """ Return the digest value MD5 as a string of hexadecimal digits. """
    object_encode_name = str(_object).encode()
    object_encode_type = str(type(_object)).encode()
    object_hash = hashlib.md5(object_encode_name + object_encode_type)
    return object_hash.hexdigest()


def build_hash(*args, **kwargs) -> str:
    """
    Method that build a unique and unrepeatable key to the state of an object
    :param args: Input object.
    :return: [String] Unique key (hash) of the object
    """
    hash_multiple = ''
    for arg in args:
        hash_multiple += kwargs.get('type', _md5)(arg)
    return hash_multiple
