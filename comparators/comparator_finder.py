import logging
import re
from logging.config import dictConfig

from custom_exceptions.runtime import UnknownOrMissingComparatorError
from settings import get_logging_config

# Logging configuration
dictConfig(get_logging_config(process_name=__name__))
logger = logging.getLogger()


class ComparatorAndVersionSeparator(object):
    def __init__(self, version_string):
        self._version_string = version_string

    def get_comparator_and_version_strings(self):
        match = re.search('\d', self._version_string)
        if match and match.start() > 0:
            start_position = match.start()
            comparator_string = self._version_string[:start_position]
            trimmed_version_string = self._version_string[start_position:]
            logger.info('Found comparator "{comparator_string}" and version "{trimmed_version_string}" in string '
                        '"{version_string}"'.format(comparator_string=comparator_string,
                                                  trimmed_version_string=trimmed_version_string,
                                                  version_string=self._version_string))
            return comparator_string, trimmed_version_string
        else:
            raise UnknownOrMissingComparatorError('Could not locate comparator in version string '
                                                  '{version_string}'.format(version_string=self._version_string))
