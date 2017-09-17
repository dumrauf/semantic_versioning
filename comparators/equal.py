from comparators.basic_comparator import BasicComparator


class Equal(BasicComparator):
    SYMBOL = '='

    def compare(self, version_1, version_2):
        return version_1 == version_2

