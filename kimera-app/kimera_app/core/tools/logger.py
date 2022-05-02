import logging.config

from kimera_core.components.tools.utils.constants import KIMERA_LOGGER_NAME
from kimera_core.components.tools.utils.logger import DICT_CONFIG

if __name__ == "__main__":
    # -------------------------------------------------------------------
    # ------------------------- EXAMPLES --------------------------------
    # -------------------------------------------------------------------

    logging.config.dictConfig(DICT_CONFIG)
    kimera_logger = logging.getLogger(KIMERA_LOGGER_NAME)
    kimera_logger.info("info")
    kimera_logger.debug("debug")
    kimera_logger.error("error")
