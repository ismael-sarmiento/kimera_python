from kimera_core.components.engines.raw import extractors as kimera_core_extractors
from kimera_core.components.engines.raw import loaders as kimera_core_loaders
from kimera_core.components.engines.raw import transformers as kimera_core_transformers


def extractor():
    return kimera_core_extractors


def transformer():
    return kimera_core_transformers


def loader():
    return kimera_core_loaders
