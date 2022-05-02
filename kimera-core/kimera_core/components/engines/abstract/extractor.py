from abc import ABC, abstractmethod


class Extractor(ABC):
    """ Abstract class that defines how to extract an object """

    @abstractmethod
    def read(self, **kwargs) -> object:
        """ Extractor method """
