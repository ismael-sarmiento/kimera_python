"""
This module contains different logger handlers
Documentation: https://docs.python.org/3/library/logging.html
"""

import logging
from logging.handlers import DatagramHandler

DICT_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'stream': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
        'file': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
        'logstash': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'stream_handler': {
            'level': 'DEBUG',
            'formatter': 'stream',
            'class': 'logging.StreamHandler',
        },
        # 'file_handler': {
        #     'level': 'ERROR',
        #     'filename': 'records.log',
        #     'class': 'logging.FileHandler',
        #     'formatter': 'file'
        # },
        'logstash_handler': {
            'level': 'INFO',
            'class': 'components.tools.utils.logger.KimeraLogstashHandler',
            'host': 'localhost',
            'port': 9998,
            'formatter': 'logstash'
        }
    },
    'loggers': {
        'logger1': {
            'handlers': ['stream_handler', 'logstash_handler'],
            'level': 'DEBUG',
            'propagate': True
        },
        'logger2': {
            'handlers': ['stream_handler', 'logstash_handler'],
            'level': 'DEBUG',
            'propagate': True
        },

    }
}


class KimeraLogstashHandler(DatagramHandler):
    """ Custom DatagramHandler """

    def makePickle(self, record: logging.LogRecord) -> bytes:
        """
        Overwriting the method [see parent documentation]

        The record is serialized to bytes using the codec registered for encoding.
        :param record: [LogRecord] Record
        :return: [bytes] Serialized record
        """
        return str.encode(self.format(record))


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
