""" This module contains different implementations for pandas extractor """

from abc import ABC, abstractmethod
from typing import Union

import pandas as pd
from pandas import DataFrame
from pandas.io.parsers import TextParser

from kimera_core.components.tools.utils.generic import ExceptionsUtils


class Extractor(ABC):
    """ Abstract class that defines how to extract an object """

    @abstractmethod
    def read(self, **kwargs) -> object:
        """ Extractor method """


class PandasCSVExtractor(Extractor):
    """
    Pandas - CSV Extractor
    Reference Documentation: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
    """

    def read(self, **kwargs) -> Union[DataFrame, TextParser]:
        """
            result = pd.read_csv(filepath_or_buffer, **options)

        :param kwargs: Options.
        :return: [result] csv file into DataFrame.
        """
        ExceptionsUtils.raise_exception_if_module_not_exists('pandas')
        ExceptionsUtils.raise_exception_if_key_not_in_kwargs('filepath_or_buffer', **kwargs)
        return pd.read_csv(**kwargs)
