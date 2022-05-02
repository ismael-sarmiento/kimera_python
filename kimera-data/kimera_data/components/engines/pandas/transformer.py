""" This module contains different implementations for pandas transformer """
from abc import ABC
from typing import List, Union

import numpy
import pandas
from pandas import DataFrame, Series

from kimera_core.components.tools.utils.generic import ObjectUtils


class PandasTransformer(ABC):
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
    def set_name_attr_in_object_pandas(_object_pandas: Union[DataFrame, Series], name: str) -> object:
        _object_pandas.attrs['name'] = name
        return _object_pandas

    @staticmethod
    def object_pandas_by_names(dfs: list, names: list) -> list:
        tmp = []
        for name in names:
            for df in dfs:
                tmp.append(df) if df.attrs['name'] == name else None
        return tmp

    @staticmethod
    def set_composite_primary_key_column(df: DataFrame, composite_primary_column: list):
        composite_primary_key = PandasTransformer._COMPOSITE_PRIMARY_KEY
        separator_key_columns = PandasTransformer._SEPARATOR_KEY_COLUMNS
        df[composite_primary_key] = ""
        for column in composite_primary_column:
            df[composite_primary_key] = df[composite_primary_key].astype(str) + separator_key_columns + \
                                        df[column].astype(str)
        return df

    @staticmethod
    def intersection_between_dataframes(df_a: DataFrame, df_b: DataFrame, pk_column: str):
        df_a_isin_df_b = df_a[df_a[pk_column].isin(df_b[pk_column])]
        df_a_not_isin_df_b = df_a[~df_a[pk_column].isin(df_b[pk_column])]
        return df_a_not_isin_df_b, df_a_isin_df_b

    @staticmethod
    def replace_null_with_value(df, value, **kwargs):
        return df.where(pandas.notnull(df), other=value, **kwargs)  # df.fillna()


class PandasTransformerBasicAuditory(PandasTransformer):

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
    def __prepare_dataframes_to_build_differences(df_a_isin_df_b: DataFrame, df_b_isin_df_a: DataFrame, pk_column: str):
        df_a_isin_df_b = df_a_isin_df_b.drop_duplicates(subset=[pk_column]).reindex(
            columns=df_a_isin_df_b.columns).drop_duplicates()
        df_b_isin_df_a = df_b_isin_df_a.drop_duplicates(subset=[pk_column]).reindex(
            columns=df_b_isin_df_a.columns).drop_duplicates()
        df_a_prepared, df_b_prepared = df_a_isin_df_b.set_index(pk_column), df_b_isin_df_a.set_index(pk_column)
        return df_a_prepared, df_b_prepared

    @staticmethod
    def __build_differences(df_a_isin_df_b: DataFrame, df_b_isin_df_a: DataFrame, pk_column: str):
        df_a_isin_df_b_prepared, df_b_isin_df_a_prepared = PandasTransformerBasicAuditory. \
            __prepare_dataframes_to_build_differences(df_a_isin_df_b, df_b_isin_df_a, pk_column)
        df_with_differences = PandasTransformerBasicAuditory. \
            build_df_differences(df_a_isin_df_b_prepared, df_b_isin_df_a_prepared)
        if ObjectUtils.object_is_instance_of_class(df_with_differences, DataFrame):
            df_b_isin_df_a_modified = df_b_isin_df_a[df_b_isin_df_a[pk_column].isin(df_with_differences.reset_index().
                                                                                    pk)]
            return df_b_isin_df_a_modified, df_with_differences
        else:
            return None, None  # pd.DataFrame()

    @staticmethod
    def build_df_auditory(df_a: DataFrame, df_b: DataFrame, primary_key_column: str):
        common_columns = PandasTransformer.common_columns_between_dataframes([df_a, df_b])
        df_a, df_b = df_a[common_columns], df_b[common_columns]
        df_a_not_isin_df_b, df_a_isin_df_b = PandasTransformer. \
            intersection_between_dataframes(df_a, df_b, primary_key_column)
        df_b_not_isin_df_a, df_b_isin_df_a = PandasTransformer. \
            intersection_between_dataframes(df_b, df_a, primary_key_column)
        df_b_isin_df_a_modified, df_with_detail_differences = PandasTransformerBasicAuditory. \
            __build_differences(df_a_isin_df_b, df_b_isin_df_a, primary_key_column)
        return df_a_not_isin_df_b, df_b_not_isin_df_a, df_b_isin_df_a_modified, df_with_detail_differences


class PandasTransformerBasicPrelation(PandasTransformer):

    @staticmethod
    def __prepare_df_output(prelation_info: dict, output_index: Series):
        output_columns = list(prelation_info.keys())
        df_output = pandas.DataFrame(columns=output_columns)
        df_output[PandasTransformer._COMPOSITE_PRIMARY_KEY] = output_index
        df_output = df_output.set_index(output_index).drop(columns=PandasTransformer._COMPOSITE_PRIMARY_KEY)
        return df_output, output_columns

    @staticmethod
    def __prepare_prelation_inputs(prelation_inputs: list, composite_primary_column: list):
        prelation_inputs = [
            PandasTransformer.set_composite_primary_key_column(prelation_input, composite_primary_column)
            for prelation_input in prelation_inputs]
        output_index = pandas.concat([prelation_input[PandasTransformer._COMPOSITE_PRIMARY_KEY]
                                      for prelation_input in prelation_inputs]).drop_duplicates()
        prelation_inputs = [prelation_input.set_index(prelation_input[PandasTransformer._COMPOSITE_PRIMARY_KEY]).
                                drop(columns=PandasTransformer._COMPOSITE_PRIMARY_KEY) for prelation_input in
                            prelation_inputs]
        return prelation_inputs, output_index

    @staticmethod
    def prelation_external(compose_primary_key: list, prelation_inputs: list, prelation_info: dict) -> DataFrame:
        prelation_inputs, output_index = PandasTransformerBasicPrelation.__prepare_prelation_inputs(prelation_inputs,
                                                                                                    compose_primary_key)
        df_output, output_columns = PandasTransformerBasicPrelation.__prepare_df_output(prelation_info, output_index)
        for output_column in output_columns:
            prelation_input_names = prelation_info[output_column]
            prelation_inputs_by_column = PandasTransformer. \
                object_pandas_by_names(prelation_inputs, prelation_input_names)
            for prelation_input in prelation_inputs_by_column:
                df_output_null = df_output.loc[df_output[output_column].isna(), [output_column]]
                if not df_output_null.empty:
                    df_prelation = df_output_null.merge(prelation_input[[output_column]],
                                                        on=PandasTransformer._COMPOSITE_PRIMARY_KEY,
                                                        how='inner', suffixes=('_primary', '_secondary'),
                                                        indicator=True)
                    df_output.loc[df_output[output_column].isna(), output_column] = df_prelation[
                        output_column + '_secondary']
        df_output = df_output.reset_index(drop=True)
        return df_output
