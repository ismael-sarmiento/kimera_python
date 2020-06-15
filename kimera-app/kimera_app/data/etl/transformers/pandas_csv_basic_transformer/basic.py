import kimera_data.components.etl as kimera_etl
from kimera_data.components.engines.pandas.transformers import PandasTransformer


def extract_data_a():
    extractor = kimera_etl.extractor(). \
        engine('pandas'). \
        format('csv'). \
        option("filepath_or_buffer", 'basic.csv'). \
        option('sep', ';')
    return extractor.read()


def extract_data_b():
    extractor = kimera_etl.extractor(). \
        engine('pandas'). \
        format('csv'). \
        option("filepath_or_buffer", 'basicI.csv'). \
        option('sep', ';')
    return extractor.read()


def transform_data_shape(_object):
    transformer = kimera_etl.transformer(). \
        input_data(_object). \
        apply(PandasTransformer.shape, PandasTransformer.shape)
    return transformer.transform()


def transform_data_df_auditory(_object_a, _object_b, pk_column):
    transformer = kimera_etl.transformer(). \
        input_data(_object_a, _object_b, pk_column=pk_column). \
        apply(PandasTransformer.build_df_auditory)
    return transformer.transform()


def transform_data_shape_size(_object):
    transform = kimera_etl.transformer(). \
        input_data(_object). \
        apply(PandasTransformer.shape, PandasTransformer.size)
    return transform.transform()


if __name__ == '__main__':
    data_a, data_b = extract_data_a(), extract_data_b()
    print(f"\nResult I: {transform_data_shape(data_a)}")
    print(f"\nResult II: {transform_data_df_auditory(data_a, data_b, pk_column='Nombre')}")
    print(f"\nResult III: {transform_data_shape_size(data_a)}")
