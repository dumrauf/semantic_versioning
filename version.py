from custom_exceptions.runtime import IncorrectVersionNumberError


class Version(object):
    @staticmethod
    def _parse_version_string(version_string):
        sub_versions = version_string.split('.')
        try:
            int_sub_versions = [int(sub_version) for sub_version in sub_versions]
        except ValueError as e:
            raise IncorrectVersionNumberError('{version_string} could does not consist of solely integers '
                                              'separated by dots'.format(version_string=version_string))
        return int_sub_versions

    def __init__(self, version_string):
        self._version_string = version_string
        self._parsed_version_string = self._parse_version_string(version_string=version_string)

    def __eq__(self, other):
        return self._parsed_version_string == other._parsed_version_string

    def __ge__(self, other):
        return self._parsed_version_string >= other._parsed_version_string

    def __gt__(self, other):
        return self._parsed_version_string > other._parsed_version_string
