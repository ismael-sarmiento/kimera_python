"""
This module contains different logger handlers
Documentation: https://docs.python.org/3/library/logging.html
"""

# ----- LOGGER BY DICT_CONFIG ----- #
DICT_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'stream_formatter_basic': {
            'format': '%(asctime)s - %(levelname)s - %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'stream_formatter_advanced': {
            'format': '%(asctime)s - %(name)s - %(threadName)s - %(thread)d - %(levelname)s - %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'logstash': {
            'format': '%(asctime)s - %(name)s - %(threadName)s - %(thread)d - %(levelname)s - %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'handlers': {
        'stream_handler_basic': {
            'level': 'DEBUG',
            'formatter': 'stream_formatter_basic',
            'class': 'logging.StreamHandler',
        },
        'stream_handler_advanced': {
            'level': 'DEBUG',
            'formatter': 'stream_formatter_advanced',
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'kimera-core-basic': {
            'handlers': ['stream_handler_basic'],
            'level': 'DEBUG',
            'propagate': True
        },
        'kimera-core-advanced': {
            'handlers': ['stream_handler_advanced'],
            'level': 'DEBUG',
            'propagate': True
        },

    }
}
