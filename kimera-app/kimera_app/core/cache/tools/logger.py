from kimera_core.components.tools.utils.logger import DICT_CONFIG

if __name__ == "__main__":
    # -------------------------------------------------------------------
    # ------------------------- EXAMPLES --------------------------------
    # -------------------------------------------------------------------

    import logging
    import logging.config

    logging.config.dictConfig(DICT_CONFIG)
    logger1 = logging.getLogger('logger1')
    logger2 = logging.getLogger('logger2')
    logger1.info("aqui")
    logger1.debug("aqui")
    logger1.error("esto es un error")

    logger2.info("aqui")
    logger2.debug("aqui")
    logger2.error("esto es un error")
