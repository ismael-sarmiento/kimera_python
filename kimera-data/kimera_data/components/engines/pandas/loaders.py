""" This module contains different implementations for pandas loader """
from pandas import DataFrame

from kimera_core.components.tools.utils.generic import ExceptionsUtils


class PandasCSVLoader:
    """ Pandas - Loader """

    @staticmethod
    def to_csv(df: DataFrame, **kwargs):
        """
            result = Dataframe.to_csv(filepath_or_buffer, **options)

            Reference Documentation: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html

        :param df: DataFrame
        :param kwargs: Options.
        :return: [result] csv file into DataFrame.
        """
        ExceptionsUtils.raise_exception_if_module_not_exists('pandas')
        ExceptionsUtils.raise_exception_if_key_not_in_kwargs('filepath_or_buffer', **kwargs)
        df.to_csv(**kwargs)
