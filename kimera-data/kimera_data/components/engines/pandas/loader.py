""" This module contains different implementations for pandas loader """
from pandas import DataFrame

from kimera_core.components.tools.utils.generic import ExceptionsUtils


class PandasCSVLoader:
    """ Pandas - Loader """

    @staticmethod
    def to_csv(df: DataFrame, **kwargs):
        """
        https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html

            result = Dataframe.to_csv(filepath_or_buffer, **options)

        :df: DataFrame
        :kwargs: Options.
        :return: [None or str] If path_or_buf is None, returns the resulting csv format as a string.
                 Otherwise, returns None.
        """
        ExceptionsUtils.raise_exception_if_module_not_exists('pandas')
        ExceptionsUtils.raise_exception_if_key_not_in_kwargs('filepath_or_buffer', **kwargs)
        return df.to_csv(**kwargs)
