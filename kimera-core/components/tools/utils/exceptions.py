""" This module contains different exceptions utility tools """


class ExceptionsUtils:
    """ Exceptions utils class """

    @staticmethod
    def raise_exception_if_key_not_in_dict(key, _dict):
        if key not in _dict:
            raise Exception(f'Key {key} not defined in options. Please define it!')
