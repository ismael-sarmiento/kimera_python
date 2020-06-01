""" This module contains different implementations for raw extraction """

from abc import ABC, abstractmethod

from components.tools.utils.exceptions import ExceptionsUtils


class Extractor(ABC):
    """ Abstract class that defines how to extract an object """

    @abstractmethod
    def read(self, **kwargs) -> object:
        """ Extractor method """


class RawZipExtractor(Extractor):
    """ Raw - Zip Extractor """

    def read(self, **kwargs) -> list:
        ExceptionsUtils.raise_exception_if_key_not_in_dict('filename', kwargs)
        return self._file_descriptors(**kwargs)

    @staticmethod
    def _file_descriptors(**kwargs) -> list:
        from zipfile import ZipFile
        with ZipFile(**kwargs) as z:
            return [z.open(file) for file in z.namelist()]
