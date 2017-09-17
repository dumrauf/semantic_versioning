from unittest import TestCase

from comparators.basic_comparator import BasicComparator
from custom_exceptions.configuration import ImproperlyConfiguredError


class ImproperlyConfiguredComparator(BasicComparator):
    pass


class TestBasicComparator(TestCase):
    def test_improperly_configured_comparator(self):
        self.assertRaises(ImproperlyConfiguredError, ImproperlyConfiguredComparator)
