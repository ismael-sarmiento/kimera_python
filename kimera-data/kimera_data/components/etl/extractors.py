from typing import List, Iterable

from kimera_core.components.engines.raw.extractors import RawZipExtractor
from kimera_core.components.tools.utils.generic import ExceptionsUtils, ObjectUtils
from kimera_data.components.engines.pandas.extractor import PandasCSVExtractor
from kimera_db.components import create_table_if_not_exist as kimera_db_create_table_if_not_exist

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
        self.__engine = None
        self.__format = None
        self.__options = dict()
        self.__extractors = list()

    def engine(self, engine: str):
        self.__engine = engine
        return self

    def format(self, fmt: str):
        self.__format = fmt
        return self

    def option(self, key, value):
        self.__options[key] = value
        return self

    def options(self, options: dict):
        self.__options.update(options)
        return self

    def create_table_if_not_exist(self, source_data, dialect, driver_name, username, password, host, port, database,
                                  limit, query_list, table_name):
        kimera_db_create_table_if_not_exist(source_data, dialect, driver_name, username, password, host, port, database,
                                            limit, query_list, table_name)
        return self

    def multiple(self, extractors: Iterable[List['ETLExtractor']]):
        if not (extractors and ObjectUtils.internal_objects_of_iterable_are_instances_of_class(extractors,
                                                                                               ETLExtractor) and
                ObjectUtils.object_is_instance_of_class(extractors, list)):
            raise TypeError("Input parameters must be of type ETLExtractor 'list'.")
        self.__extractors = extractors
        return self

    def read(self):
        if hasattr(self, '__extractors') and self.__extractors:
            return self.__multi_read()
        else:
            return self.__single_read()

    def clear(self):
        self.__engine = None
        self.__format = None
        self.__options = dict()
        self.__extractors = list()

    def __single_read(self):
        data = self.__extract_data()
        return data

    def __multi_read(self):
        data = [extractor.read() for extractor in self.__extractors]
        return data

    def __build_options(self):
        options = self.__options
        return options

    def __extract_data(self):
        ExceptionsUtils.raise_exception_if_attr_not_defined(self, '__engine')
        ExceptionsUtils.raise_exception_if_attr_not_defined(self, '__format')
        options = self.__build_options()
        data = FactoryExtractors().get_extractor(engine=self.__engine, fmt=self.__format).read(**options)
        return data
