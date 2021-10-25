""" This module contains different implementations for raw extraction """

from abc import ABC, abstractmethod

from kimera_core.components.tools.utils.generic import ExceptionsUtils


class Extractor(ABC):
    """ Abstract class that defines how to extract an object """

    @abstractmethod
    def read(self, **kwargs) -> object:
        """ Extractor method """


class RawZipExtractor(Extractor):
    """ Raw - Zip Extractor

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

        :param kwargs: Options.
        :return: [result] Reading internal zip file.
        """
        ExceptionsUtils.raise_exception_if_key_not_in_kwargs('file', **kwargs)
        return self._file_descriptors(**kwargs)

    @staticmethod
    def _file_descriptors(**kwargs) -> list:
        from zipfile import ZipFile
        with ZipFile(**kwargs) as z:
            return [z.open(file) for file in z.namelist()]


class RawJsonExtractor(Extractor):
    """ Raw - JSON Extractor

    Deserialize ``fp=file_path`` (a ``.read()``-supporting file-like object containing
    a JSON document) to a Python object.

    ``object_hook`` is an optional function that will be called with the
    result of any object literal decode (a ``dict``). The return value of
    ``object_hook`` will be used instead of the ``dict``. This feature
    can be used to implement custom decoders (e.g. JSON-RPC class hinting).

    ``object_pairs_hook`` is an optional function that will be called with the
    result of any object literal decoded with an ordered list of pairs.  The
    return value of ``object_pairs_hook`` will be used instead of the ``dict``.
    This feature can be used to implement custom decoders.  If ``object_hook``
    is also defined, the ``object_pairs_hook`` takes priority.

    To use a custom ``JSONDecoder`` subclass, specify it with the ``cls``
    kwarg; otherwise ``JSONDecoder`` is used.
    """

    def read(self, **kwargs) -> object:
        """
            j = json.load(fp, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None,
                          object_pairs_hook=None, **kw)

            result = json.load(**kwargs)

        :param kwargs: Options.
        :return: [result] Reading internal json file.
        """
        import json
        ExceptionsUtils.raise_exception_if_key_not_in_kwargs('fp', **kwargs)
        return json.load(**kwargs)
