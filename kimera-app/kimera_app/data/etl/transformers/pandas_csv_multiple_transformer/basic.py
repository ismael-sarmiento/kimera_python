import kimera_data.components.etl as kimera_etl
from kimera_data.components.engines.pandas.transformers import PandasTransformer


def extract_csv_file():
    extractor = kimera_etl.extractor().engine('pandas').format('csv').option("filepath_or_buffer", 'basic.csv').option('sep', ';')
    return extractor.read()


def transform_csv_file(_object):
    transform = kimera_etl.transformer().input_data(_object).apply(PandasTransformer.shape)
    return transform


def transforms_csv_file(_object):
    transform = kimera_etl.transformer().input_data(_object).apply(PandasTransformer.shape, PandasTransformer.shape)
    return transform


if __name__ == '__main__':
    data = extract_csv_file()
    transformer = transform_csv_file(data)
    transformers = transforms_csv_file(data)
    transformed_data = kimera_etl.transformer().multiple([transformer, transformers]).transform()
    print(transformed_data)
