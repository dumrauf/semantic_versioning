from version_comparator import VersionComparator


def compare(version_1, version_2):
    version_comparator = VersionComparator(version_1=version_1,
                                           version_2=version_2)
    return version_comparator.compare_versions()
