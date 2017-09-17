import os
from errno import EEXIST

__author__ = 'dominic'


# Directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIRECTORY = os.path.join(BASE_DIR, '.logs')

# Bootstrap all required directories
for directory in [LOG_DIRECTORY]:
    try:
        os.makedirs(directory)
    except OSError as e:
        if e.errno == EEXIST:
            pass
        else:
            raise e


INFO_LOG_NAME = 'info.log'
ERROR_LOG_NAME = 'error.log'


def get_logging_config(process_name):
    return {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'simple': {
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            }
        },

        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'level': 'DEBUG',
                'formatter': 'simple',
                'stream': 'ext://sys.stdout'
            },

            'info_file_handler': {
                'class': 'logging.handlers.RotatingFileHandler',
                'level': 'INFO',
                'formatter': 'simple',
                'filename': os.path.join(LOG_DIRECTORY,
                                         '{process_name}_{INFO_LOG_NAME}'.format(process_name=process_name,
                                                                                 INFO_LOG_NAME=INFO_LOG_NAME)),
                'maxBytes': 10485760,
                'backupCount': 20,
                'encoding': 'utf8'
            },

            'error_file_handler': {
                'class': 'logging.handlers.RotatingFileHandler',
                'level': 'ERROR',
                'formatter': 'simple',
                'filename': os.path.join(LOG_DIRECTORY,
                                         '{process_name}_{ERROR_LOG_NAME}'.format(process_name=process_name,
                                                                                  ERROR_LOG_NAME=ERROR_LOG_NAME)),
                'maxBytes': 10485760,
                'backupCount': 20,
                'encoding': 'utf8'
            }
        },

        'loggers': {
            'my_module': {
                'level': 'ERROR',
                'handlers': ['console'],
                'propagate': 'no'
            }
        },

        'root': {
            'level': 'INFO',
            'handlers': ['console',
                         'info_file_handler',
                         'error_file_handler']
        }
    }
