from comparators.greater_equal import GreaterEqual
from tests.basic_test_versions import BasicTestVersions


class TestGreaterEqualVersion(BasicTestVersions):
    COMPARATOR_SYMBOL = '>='
    COMPARATOR_KLASS = GreaterEqual

    def _handle_version_1_and_version_2_same_length_and_equal(self, compare_version_result):
        return self.assertTrue(compare_version_result)

    def _handle_version_1_and_version_2_same_length_but_version_1_smaller(self, compare_version_result):
        return self.assertTrue(compare_version_result)

    def _handle_version_1_and_version_2_same_length_but_version_1_larger(self, compare_version_result):
        return self.assertFalse(compare_version_result)

    def _handle_version_1_shorter_than_version_2_but_version_1_smaller(self, compare_version_result):
        return self.assertTrue(compare_version_result)

    def _handle_version_1_shorter_than_version_2_but_version_1_larger(self, compare_version_result):
        return self.assertFalse(compare_version_result)

    def _handle_version_1_longer_than_version_2_but_version_1_larger(self, compare_version_result):
        return self.assertFalse(compare_version_result)

    def _handle_version_1_longer_than_version_2_but_version_1_smaller(self, compare_version_result):
        return self.assertTrue(compare_version_result)
