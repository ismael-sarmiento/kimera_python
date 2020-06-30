""" This module contains different implementations for pandas transformer """
from typing import List

import numpy
import pandas
from pandas import DataFrame

from kimera_core.components.tools.utils.generic import ObjectUtils


class PandasTransformer:
    _COMPOSITE_PRIMARY_KEY = "COMPOSITE_PRIMARY_KEY"
    _SEPARATOR_KEY_COLUMNS = "#"

    @staticmethod
    def size(object_pandas) -> int:
        """
            Return an int representing the number of elements in this object.

            Return the number of rows if Series. Otherwise return the number of rows times number of columns if DataFrame.

        :param object_pandas: Object creates by pandas.
        :return: [Int] Response.
        """
        return object_pandas.size

    @staticmethod
    def shape(object_pandas) -> object:
        """
            Return a tuple representing the dimensionality of the DataFrame.

        :param object_pandas: Object creates by pandas.
        :return: [Tuple] (number_of_rows, number_of_columns) Response.
        """
        return object_pandas.shape

    @staticmethod
    def common_columns_between_dataframes(dfs: List['DataFrame']) -> list:
        """ This returns a Index with column common between the df_a and df_b. """
        columns = []
        for df_a, df_b in zip(dfs, dfs[1:]):
            intersection = df_a.columns.intersection(df_b.columns)
            [columns.append(i) for i in intersection]
        return list(set(columns))

    @staticmethod
    def set_composite_primary_key_column(df: DataFrame, composite_primary_column: list):
        COMPOSITE_PRIMARY_KEY = PandasTransformer._COMPOSITE_PRIMARY_KEY
        SEPARATOR_KEY_COLUMNS = PandasTransformer._SEPARATOR_KEY_COLUMNS
        df[COMPOSITE_PRIMARY_KEY] = ""
        for column in composite_primary_column:
            df[COMPOSITE_PRIMARY_KEY] = df[COMPOSITE_PRIMARY_KEY].astype(str) + SEPARATOR_KEY_COLUMNS + df[column].astype(str)
        return df

    @staticmethod
    def intersection_between_dataframes(df_a: DataFrame, df_b: DataFrame, pk_column: str):
        df_a_isin_df_b = df_a[df_a[pk_column].isin(df_b[pk_column])]
        df_a_not_isin_df_b = df_a[~df_a[pk_column].isin(df_b[pk_column])]
        return df_a_not_isin_df_b, df_a_isin_df_b

    @staticmethod
    def build_df_differences(df_a_isin_df_b_prepared: DataFrame, df_b_isin_df_a_prepared: DataFrame):
        if not df_a_isin_df_b_prepared.equals(df_b_isin_df_a_prepared):
            diff_mask = (df_a_isin_df_b_prepared != df_b_isin_df_a_prepared) & \
                        ~(df_a_isin_df_b_prepared.isnull() & df_b_isin_df_a_prepared.isnull())
            ne_stacked = diff_mask.stack()
            changed = ne_stacked[ne_stacked]
            changed.index.names = ['pk', 'column_changed']
            difference_locations = numpy.where(diff_mask)
            changed_from = df_a_isin_df_b_prepared.values[difference_locations]
            changed_to = df_b_isin_df_a_prepared.values[difference_locations]
            data = {'new_value': changed_to, 'old_value': changed_from}
            columns = ['new_value', 'old_value']
            index = changed.index
            df_differences = pandas.DataFrame(data=data, columns=columns, index=index).reset_index()
            return df_differences

    @staticmethod
    def _prepare_dataframes_to_build_differences(df_a_isin_df_b: DataFrame, df_b_isin_df_a: DataFrame, pk_column: str):
        df_a_isin_df_b = df_a_isin_df_b.drop_duplicates(subset=[pk_column]).reindex(columns=df_a_isin_df_b.columns).drop_duplicates()
        df_b_isin_df_a = df_b_isin_df_a.drop_duplicates(subset=[pk_column]).reindex(columns=df_b_isin_df_a.columns).drop_duplicates()
        df_a_prepared, df_b_prepared = df_a_isin_df_b.set_index(pk_column), df_b_isin_df_a.set_index(pk_column)
        return df_a_prepared, df_b_prepared

    @staticmethod
    def _build_differences(df_a_isin_df_b: DataFrame, df_b_isin_df_a: DataFrame, pk_column: str):
        df_a_isin_df_b_prepared, df_b_isin_df_a_prepared = PandasTransformer._prepare_dataframes_to_build_differences(
            df_a_isin_df_b, df_b_isin_df_a, pk_column)
        df_with_differences = PandasTransformer.build_df_differences(df_a_isin_df_b_prepared, df_b_isin_df_a_prepared)
        if ObjectUtils.object_is_instance_of_class(df_with_differences, DataFrame):
            df_b_isin_df_a_modified = df_b_isin_df_a[df_b_isin_df_a[pk_column].isin(df_with_differences.reset_index().pk)]
            return df_b_isin_df_a_modified, df_with_differences
        else:
            return None, None

    @staticmethod
    def build_df_auditory(df_a: DataFrame, df_b: DataFrame, pk_column: str):
        common_columns = PandasTransformer.common_columns_between_dataframes([df_a, df_b])
        df_a, df_b = df_a[common_columns], df_b[common_columns]
        df_a_not_isin_df_b, df_a_isin_df_b = PandasTransformer.intersection_between_dataframes(df_a, df_b, pk_column)
        df_b_not_isin_df_a, df_b_isin_df_a = PandasTransformer.intersection_between_dataframes(df_b, df_a, pk_column)
        df_b_isin_df_a_modified, df_with_detail_differences = PandasTransformer._build_differences(df_a_isin_df_b, df_b_isin_df_a, pk_column)
        return df_a_not_isin_df_b, df_b_not_isin_df_a, df_b_isin_df_a_modified, df_with_detail_differences
