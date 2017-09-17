from comparators.basic_comparator import BasicComparator


class GreaterEqual(BasicComparator):
    SYMBOL = '>='

    def compare(self, version_1, version_2):
        return version_2 >= version_1

