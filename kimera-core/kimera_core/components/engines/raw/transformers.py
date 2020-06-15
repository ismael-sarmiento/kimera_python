""" This module contains different implementations for python transformer """


class RawTransformer:

    @staticmethod
    def intersection_lists(a: list, b: list) -> list:
        return list(set(a).intersection(b))
