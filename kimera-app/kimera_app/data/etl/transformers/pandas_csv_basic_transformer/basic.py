import kimera_data.components.etl as kimera_etl
from kimera_data.components.engines.pandas.transformer import PandasTransformerBasic, PandasTransformerBasicAuditory


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
        apply(PandasTransformerBasic.shape, PandasTransformerBasic.shape)
    return transformer.transform()


def transform_data_df_auditory(_object_a, _object_b, primary_key_column):
    transformer = kimera_etl.transformer(). \
        input_data(_object_a, _object_b, primary_key_column=primary_key_column). \
        apply(PandasTransformerBasicAuditory.build_df_auditory)
    return transformer.transform()


if __name__ == '__main__':
    data_a, data_b = extract_data_a(), extract_data_b()
    data_c = transform_data_df_auditory(data_a, data_b, primary_key_column='Nombre')
