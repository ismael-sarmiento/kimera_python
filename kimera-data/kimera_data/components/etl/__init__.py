from kimera_data.components.etl.extractor import ETLExtractor
from kimera_data.components.etl.transformer import ETLTransformer


def extractor():
    return ETLExtractor()


def transformer():
    return ETLTransformer()
