""" This module contains different implementations for python transformer """


class RawTransformer:
    """ Raw - Transformer """

    @staticmethod
    def intersection_lists(a: list, b: list) -> list:
        """ Return the intersection of two list as a new list """
        return list(set(a).intersection(b))
