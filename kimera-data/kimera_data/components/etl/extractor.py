from typing import List, Iterable

from kimera_core.components.engines.raw.extractors import RawZipExtractor
from kimera_core.components.tools.utils.generic import ExceptionsUtils, ObjectUtils
from kimera_data.components.engines.pandas.extractors import PandasCSVExtractor

_EXTRACTORS = {
    'raw': {
        'zip': RawZipExtractor
    },
    'pandas': {
        'csv': PandasCSVExtractor
    },
}


class FactoryExtractors:

    def __init__(self):
        self.extractors = _EXTRACTORS

    def get_extractor(self, engine, fmt):
        return self.extractors[engine][fmt]()


class ETLExtractor:

    def __init__(self):
        self._engine = None
        self._format = None
        self._options = dict()
        self._extractors = list()

    def engine(self, engine):
        self._engine = engine
        return self

    def format(self, fmt):
        self._format = fmt
        return self

    def option(self, key, value):
        self._options[key] = value
        return self

    def multiple(self, extractors: Iterable[List['ETLExtractor']]):
        if not (extractors and ObjectUtils.internal_objects_of_iterable_are_instances_of_class(extractors, ETLExtractor) and
                ObjectUtils.object_is_instance_of_class(extractors, list)):
            raise TypeError("Input parameters must be of type ETLExtractor 'list'.")
        self._extractors = extractors
        return self

    def read(self):
        if hasattr(self, '_extractors') and self._extractors:
            return self._multi_read()
        else:
            return self._single_read()

    def _single_read(self):
        data = self._extract_data()
        return data

    def _multi_read(self):
        data = [extractor.read() for extractor in self._extractors]
        return data

    def _build_options(self):
        options = self._options
        return options

    def _extract_data(self):
        ExceptionsUtils.raise_exception_if_attr_not_defined(self, '_engine')
        ExceptionsUtils.raise_exception_if_attr_not_defined(self, '_format')
        options = self._build_options()
        data = FactoryExtractors().get_extractor(engine=self._engine, fmt=self._format).read(**options)
        return data

    def clear(self):
        self._engine = None
        self._format = None
        self._options = dict()
        self._extractors = list()
