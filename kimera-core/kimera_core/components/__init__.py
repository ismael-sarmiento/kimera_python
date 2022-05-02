""" kimera-core package initialization """

import logging.config

from kimera_core.components.tools.utils.logger import DICT_CONFIG

# Logger Initialization
logging.config.dictConfig(DICT_CONFIG)
