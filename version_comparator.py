import logging
from logging.config import dictConfig

from comparators.comparator_finder import ComparatorAndVersionSeparator
from comparators.equal import Equal
from comparators.greater_equal import GreaterEqual
from comparators.strictly_greater import StrictlyGreater
from custom_exceptions.runtime import UnknownOrMissingComparatorError
from settings import get_logging_config
from version import Version

# Logging configuration
dictConfig(get_logging_config(process_name=__name__))
logger = logging.getLogger()


KNOWN_SYMBOLS_TO_COMPARATORS_MAPPING = {
    StrictlyGreater.SYMBOL: StrictlyGreater,
    GreaterEqual.SYMBOL: GreaterEqual,
    Equal.SYMBOL: Equal,
}


class VersionComparator(object):
    def __init__(self, version_1, version_2):
        self.version_1 = version_1
        self.version_2 = version_2

    def _get_comparator_and_version_strings(self, comparator_and_version_string):
        comparator_finder = ComparatorAndVersionSeparator(version_string=comparator_and_version_string)
        return comparator_finder.get_comparator_and_version_strings()

    def _get_comparator_klass(self, comparator_string):
        try:
            comparator_klass = KNOWN_SYMBOLS_TO_COMPARATORS_MAPPING[comparator_string]
            logger.info('Found matching class "{comparator_klass}" for '
                        'string "{comparator_string}"'.format(comparator_klass=comparator_klass,
                                                              comparator_string=comparator_string))
            return comparator_klass
        except KeyError as e:
            raise UnknownOrMissingComparatorError('Unknown comparator {comparator_string}. '
                                                  'Known comparators are {known_symbols}'.format(comparator_string=comparator_string,
                                                                                                 known_symbols=KNOWN_SYMBOLS_TO_COMPARATORS_MAPPING.keys()))


    def compare_versions(self):
        comparator_string, version_1_string = self._get_comparator_and_version_strings(comparator_and_version_string=self.version_1)
        comparator_klass = self._get_comparator_klass(comparator_string=comparator_string)
        comparator = comparator_klass()
        version_1 = Version(version_string=version_1_string)
        version_2 = Version(version_string=self.version_2)
        result = comparator.compare(version_1=version_1,
                                    version_2=version_2)
        logger.info('Comparing Versions:  {version_2} {comparator} {version_1_string} : '
                    '{result}'.format(version_2=self.version_2,
                                      version_1_string=version_1_string,
                                      comparator=comparator_klass.SYMBOL,
                                      result=result))
        return result
