import kimera_data.components.etl as kimera_etl
from kimera_data.components.engines.pandas.transformer import PandasTransformerBasic, PandasTransformerBasicPrelation


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


def prelation_dict():
    return {'Nombre': ['data_b', 'data_a'],
            'Apellidos': ['data_a', 'data_b'],
            'Edad': ['data_b', 'data_b'],
            'Sexo': ['data_a'],
            'Others': ['data_b', 'data_a']}


if __name__ == '__main__':
    data_a, data_b = extract_data_a(), extract_data_b()
    data_a = kimera_etl.transformer().input_data(data_a, 'data_a').apply(
        PandasTransformerBasic.set_name_attr_in_object_pandas).transform()
    data_b = kimera_etl.transformer().input_data(data_b, 'data_b').apply(
        PandasTransformerBasic.set_name_attr_in_object_pandas).transform()
    data_c = kimera_etl.transformer().input_data(['Nombre'], [data_b[0], data_a[0]], prelation_dict()). \
        apply(PandasTransformerBasicPrelation.prelation_external).transform()  # TODO: refencia dinamica
    print(data_a, data_b, data_c)
