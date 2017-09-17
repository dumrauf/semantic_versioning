from custom_exceptions.configuration import ImproperlyConfiguredError


class BasicComparator(object):
    SYMBOL = None

    def __init__(self):
        if self.SYMBOL is None:
            raise ImproperlyConfiguredError("SYMBOL cannot be empty for a comparator.")

    def compare(self, version_1, version_2):
        raise NotImplementedError
