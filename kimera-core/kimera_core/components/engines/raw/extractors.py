""" This module contains different implementations for raw extraction """

import json
from abc import ABC, abstractmethod

from kimera_core.components.tools.utils.generic import ExceptionsUtils


class Extractor(ABC):
    """ Abstract class that defines how to extract an object """

    @abstractmethod
    def read(self, **kwargs) -> object:
        """ Extractor method """


class RawZipExtractor(Extractor):
    """ Raw - Zip Extractor

    https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile

        Class with methods to open, read, write, close, list zip files.

        z = ZipFile(file, mode="r", compression=ZIP_STORED, allowZip64=True, compresslevel=None)

    file: Either the path to the file, or a file-like object.
          If it is a path, the file will be opened and closed by ZipFile.
    mode: The mode can be either read 'r', write 'w', exclusive create 'x',
          or append 'a'.
    compression: ZIP_STORED (no compression), ZIP_DEFLATED (requires zlib),
                 ZIP_BZIP2 (requires bz2) or ZIP_LZMA (requires lzma).
    allowZip64: if True ZipFile will create files with ZIP64 extensions when
                needed, otherwise it will raise an exception when this would
                be necessary.
    compresslevel: None (default for the given compression type) or an integer
                   specifying the level to pass to the compressor.
                   When using ZIP_STORED or ZIP_LZMA this keyword has no effect.
                   When using ZIP_DEFLATED integers 0 through 9 are accepted.
                   When using ZIP_BZIP2 integers 1 through 9 are accepted.
    """

    def read(self, **kwargs) -> list:
        """
            z = ZipFile(file, mode="r", compression=ZIP_STORED, allowZip64=True, compresslevel=None)

            result = [z.open(file) for file in z.namelist()]

        kwargs: Options.
        return: [result] Reading internal zip file.
        """
        ExceptionsUtils.raise_exception_if_key_not_in_kwargs('file', **kwargs)
        return self._zip_content(**kwargs)

    @staticmethod
    def _zip_content(**kwargs) -> list:
        from zipfile import ZipFile
        with ZipFile(**kwargs) as z:
            return [z.open(file) for file in z.namelist()]


class RawJsonExtractor(Extractor):
    """ Raw - JSON Extractor

    https://docs.python.org/3/library/json.html

    Deserialize ``fp=file_path`` (a ``.read()``-supporting file-like object containing
    a JSON document) to a Python object.
    """

    def read(self, fp_or_sj: str, **kwargs) -> dict:
        """ Reader of the content of a JSON file

        https://docs.python.org/3/library/json.html#json.load

        :param fp_or_sj: Path of JSON File or String in JSON Format.
        :param kwargs: Options.
        return: [result] Reading internal json file.
        """
        try:
            with open(fp_or_sj) as f:
                json_content = json.load(f)
            return json_content
        except Exception:
            return json.loads(fp_or_sj)
