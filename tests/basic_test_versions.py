import unittest

from custom_exceptions.runtime import IncorrectVersionNumberError, UnknownOrMissingComparatorError
from main import compare


DEFAULT_COMPARATOR_SYMBOL = 'DEFAULT_COMPARATOR_SYMBOL'


class BasicTestVersions(unittest.TestCase):

    ####################################################################################################################
    # Functions to be implemented by comparator test classes - see corresponding comparators for reference
    ####################################################################################################################
    def _handle_version_1_and_version_2_same_length_and_equal(self, compare_version_result):
        # To be implemented by comparator test class
        raise NotImplementedError

    def _handle_version_1_and_version_2_same_length_but_version_1_smaller(self, compare_version_result):
        # To be implemented by comparator test class
        raise NotImplementedError

    def _handle_version_1_and_version_2_same_length_but_version_1_larger(self, compare_version_result):
        # To be implemented by comparator test class
        raise NotImplementedError

    def _handle_version_1_shorter_than_version_2_but_version_1_smaller(self, compare_version_result):
        # To be implemented by comparator test class
        raise NotImplementedError

    def _handle_version_1_shorter_than_version_2_but_version_1_larger(self, compare_version_result):
        # To be implemented by comparator test class
        raise NotImplementedError

    def _handle_version_1_longer_than_version_2_but_version_1_larger(self, compare_version_result):
        # To be implemented by comparator test class
        raise NotImplementedError

    def _handle_version_1_longer_than_version_2_but_version_1_smaller(self, compare_version_result):
        # To be implemented by comparator test class
        raise NotImplementedError

    ####################################################################################################################
    # Helper Functions for Base Class
    ####################################################################################################################
    def _format_version_1(self, version_1, comparator_symbol=DEFAULT_COMPARATOR_SYMBOL):
        if comparator_symbol == DEFAULT_COMPARATOR_SYMBOL:
            comparator_symbol = self.COMPARATOR_SYMBOL
        return '{comparator_symbol}{version_1}'.format(comparator_symbol=comparator_symbol,
                                                       version_1=version_1)
    def _compare_versions(self, versions_to_test, handler_function):
        for version_1_list, version_2_list in versions_to_test:
            version_1 = self._format_version_1(version_1_list)
            version_2 = version_2_list
            compare_version_result = compare(version_1=version_1,
                                             version_2=version_2)
            handler_function(compare_version_result=compare_version_result)

    def _compare_versions_with_exceptions(self, versions_to_test, expected_exception, comparator_symbol=DEFAULT_COMPARATOR_SYMBOL):
        for version_1_list, version_2_list in versions_to_test:
            version_1 = self._format_version_1(version_1_list,
                                               comparator_symbol=comparator_symbol)
            version_2 = version_2_list
            self.assertRaises(expected_exception, compare, version_1, version_2)

    @classmethod
    def setUpClass(cls):
        # Enable inheritance for TestCases
        if cls is BasicTestVersions:
            raise unittest.SkipTest("Skip BasicTestVersions tests on purpose")
        super(BasicTestVersions, cls).setUpClass()

    ####################################################################################################################
    # Positive Tests
    ####################################################################################################################
    def test_comparator_symbol(self):
        self.assertEqual(self.COMPARATOR_SYMBOL,
                         self.COMPARATOR_KLASS.SYMBOL)

    def test_version_1_and_version_2_same_length_and_equal(self):
        versions_to_test = [('0', '0'),
                            ('0.0', '0.0'),
                            ('1.0.0', '1.0.0'),
                            ('1.1.0.1', '1.1.0.1'),
                            ('2.0.1.8.1', '2.0.1.8.1'),
                            ('2.1.1.5.2.8', '2.1.1.5.2.8')]
        self._compare_versions(versions_to_test=versions_to_test,
                               handler_function=self._handle_version_1_and_version_2_same_length_and_equal)

    def test_version_1_and_version_2_same_length_but_version_1_smaller(self):
        versions_to_test = [('0', '1'),
                            ('0.0', '1.0'),
                            ('1.0.0', '1.0.1'),
                            ('1.1.0.1', '1.1.1.1'),
                            ('2.0.1.8.1', '2.0.2.8.1'),
                            ('2.1.1.5.2.8', '2.2.1.5.2.8')]
        self._compare_versions(versions_to_test=versions_to_test,
                               handler_function=self._handle_version_1_and_version_2_same_length_but_version_1_smaller)

    def test_version_1_and_version_2_same_length_but_version_1_larger(self):
        versions_to_test = [('1', '0'),
                            ('1.0', '0.0'),
                            ('1.0.1', '1.0.0'),
                            ('1.1.1.1', '1.1.0.1'),
                            ('2.0.2.8.1', '2.0.1.8.1'),
                            ('2.2.1.5.2.8', '2.1.1.5.2.8')]
        self._compare_versions(versions_to_test=versions_to_test,
                               handler_function=self._handle_version_1_and_version_2_same_length_but_version_1_larger)

    def test_version_1_shorter_than_version_2_but_version_1_smaller(self):
        versions_to_test = [('0', '1.0'),
                            ('0.1', '0.1.0'),
                            ('1.0.1', '1.0.1.1'),
                            ('1.1.0.1', '1.1.0.1.1'),
                            ('2.0.1.8.1', '2.1.1.8.1.1'),
                            ('2.1.1.5.2.8', '2.1.1.5.2.8.9')]
        self._compare_versions(versions_to_test=versions_to_test,
                               handler_function=self._handle_version_1_shorter_than_version_2_but_version_1_smaller)

    def test_version_1_shorter_than_version_2_but_version_1_larger(self):
        versions_to_test = [('2', '1.0'),
                            ('0.2', '0.1.0'),
                            ('1.0.2', '1.0.1.1'),
                            ('1.1.1.1', '1.1.0.1.1'),
                            ('2.2.1.8.1', '2.1.1.8.1.1'),
                            ('3.1.1.5.2.8', '2.1.1.5.2.8.9')]
        self._compare_versions(versions_to_test=versions_to_test,
                               handler_function=self._handle_version_1_shorter_than_version_2_but_version_1_larger)

    def test_version_1_longer_than_version_2_but_version_1_larger(self):
        versions_to_test = [('1.0', '0'),
                            ('0.1.0', '0.1'),
                            ('1.0.1.1', '1.0.1'),
                            ('1.1.0.1.1', '1.1.0.1'),
                            ('2.1.1.8.1.1', '2.0.1.8.1'),
                            ('2.1.1.5.2.8.9', '2.1.1.5.2.8')]
        self._compare_versions(versions_to_test=versions_to_test,
                               handler_function=self._handle_version_1_longer_than_version_2_but_version_1_larger)

    def test_version_1_longer_than_version_2_but_version_1_smaller(self):
        versions_to_test = [('1.0', '2'),
                            ('0.1.0', '0.2'),
                            ('1.0.1.1', '1.2.1'),
                            ('1.1.0.1.1', '1.9.0.1'),
                            ('2.1.1.8.1.1', '3.0.1.8.1'),
                            ('2.1.1.5.2.8.9', '2.7.1.5.2.8')]
        self._compare_versions(versions_to_test=versions_to_test,
                               handler_function=self._handle_version_1_longer_than_version_2_but_version_1_smaller)

    ####################################################################################################################
    # Negative Tests
    ####################################################################################################################
    def test_improper_version_1_but_proper_version_2_value(self):
        versions_to_test = [('1.a', '2'),
                            ('0.1f.0', '0.1'),
                            ('1..1.1', '1.2.1'),
                            ('1..3.1', '1.2.1'),
                            ('2.1.1.8.1.1.l', '3.0.1.8.1')]
        self._compare_versions_with_exceptions(versions_to_test=versions_to_test,
                                               expected_exception=IncorrectVersionNumberError)

    def test_proper_version_1_but_improper_version_2_value(self):
        versions_to_test = [('1', ''),
                            ('2', '1.a'),
                            ('0.1', '0.1f.0'),
                            ('1.2.1', '1..1.1'),
                            ('1.2.1', '1..3.1'),
                            ('3.0.1.8.1', '2.1.1.8.1.1.l')]
        self._compare_versions_with_exceptions(versions_to_test=versions_to_test,
                                               expected_exception=IncorrectVersionNumberError)

    def test_missing_comparator(self):
        versions_to_test = [('', ''),
                            ('1', ''),
                            ('2', '1.1'),
                            ('0.1', '0.1f.0'),
                            ('1.2.1', '1..1.1'),
                            ('1.2.1', '1.test.3.1'),
                            ('3.0.1.8.1', '2.1.1.8.1.1.l')]
        self._compare_versions_with_exceptions(versions_to_test=versions_to_test,
                                               expected_exception=UnknownOrMissingComparatorError,
                                               comparator_symbol='')

    def test_unknown_comparator(self):
        versions_to_test = [('', ''),
                            ('1', ''),
                            ('2', '1.1'),
                            ('0.1', '0.1f.0'),
                            ('1.2.1', '1..1.1'),
                            ('1.2.1', '1.test.3.1'),
                            ('3.0.1.8.1', '2.1.1.8.1.1.l')]
        self._compare_versions_with_exceptions(versions_to_test=versions_to_test,
                                               expected_exception=UnknownOrMissingComparatorError,
                                               comparator_symbol='<')
