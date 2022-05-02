from kimera_data.components.etl.extractors import ETLExtractor
from kimera_data.components.etl.loaders import ETLLoader
from kimera_data.components.etl.transformers import ETLTransformer


def extractor():
    return ETLExtractor()


def transformer():
    return ETLTransformer()


def loader():
    return ETLLoader()
