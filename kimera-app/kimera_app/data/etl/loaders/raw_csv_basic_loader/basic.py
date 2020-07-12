import kimera_data.components.etl as kimera_data_etl
from kimera_core.components.engines.raw.loaders import RawLoader
from kimera_data.components.engines.pandas.transformers import PandasTransformer, PandasTransformerAuditory


def extract_data_a():
    extractor = kimera_data_etl.extractor(). \
        engine('pandas'). \
        format('csv'). \
        option("filepath_or_buffer", 'basic.csv'). \
        option('sep', ';')
    return extractor.read()


def extract_data_b():
    extractor = kimera_data_etl.extractor(). \
        engine('pandas'). \
        format('csv'). \
        option("filepath_or_buffer", 'basicI.csv'). \
        option('sep', ';')
    return extractor.read()


def transform_data_shape(_object):
    transformer = kimera_data_etl.transformer(). \
        input_data(_object). \
        apply(PandasTransformer.shape, PandasTransformer.shape)
    return transformer.transform()


def transform_data_df_auditory(_object_a, _object_b, primary_key_column):
    transformer = kimera_data_etl.transformer(). \
        input_data(_object_a, _object_b, primary_key_column=primary_key_column). \
        apply(PandasTransformerAuditory.build_df_auditory)
    return transformer.transform()


def transform_data_shape_size(_object):
    transform = kimera_data_etl.transformer(). \
        input_data(_object). \
        apply(PandasTransformer.shape, PandasTransformer.size)
    return transform.transform()


def load_data_console(_object):
    loader = kimera_data_etl.loader().input_data(_object).apply(RawLoader.print_console)
    return loader.load()


if __name__ == '__main__':
    data_a, data_b = extract_data_a(), extract_data_b()
    data_a, data_c = transform_data_shape(data_a), transform_data_df_auditory(data_a, data_b, primary_key_column='Nombre')
    result = load_data_console(data_a)
