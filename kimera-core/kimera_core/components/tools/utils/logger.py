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
            'class': 'kimera_core.components.tools.utils.logger.KimeraLogstashHandler',
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
