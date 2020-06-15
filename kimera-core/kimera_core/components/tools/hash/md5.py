""" This module contains different implementations to get the hash of an object """

import hashlib


def build_hash(_obj: object) -> str:
    """
    Method that build a unique and unrepeatable key to the state of an object
    :param _obj: Input object.
    :return: [String] Unique key (hash) of the object
    """
    return hashlib.md5(str(_obj).encode() + str(type(_obj)).encode()).hexdigest()
