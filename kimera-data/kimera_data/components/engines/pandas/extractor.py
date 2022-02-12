""" This module contains different implementations ( by format ) for pandas extractor """

from typing import Union

import pandas as pd
from pandas import DataFrame
from pandas.io.parsers import TextParser

from kimera_core.components.engines.abstract.extractor import Extractor
from kimera_core.components.tools.utils.generic import ExceptionsUtils


class PandasCSVExtractor(Extractor):
    """
    Pandas - CSV Extractor
    Reference Documentation:
    """

    def read(self, **kwargs: dict) -> Union[DataFrame, TextParser]:
        """
        https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html

            result = pd.read_csv(filepath_or_buffer, **options)

        :kwargs: Options.
        :return: CSV file as DataFrame.
        """
        ExceptionsUtils.raise_exception_if_module_not_exists('pandas')
        ExceptionsUtils.raise_exception_if_key_not_in_kwargs('filepath_or_buffer', **kwargs)
        return pd.read_csv(**kwargs)
