import unittest

import apt_pkg


class TestGroup(unittest.TestCase):

    def setUp(self):
        apt_pkg.init()
        self.cache = apt_pkg.Cache()

    def test_pkgingroup(self):
        """Check that each package belongs to the corresponding group"""
        for pkg in self.cache.packages:
            group = apt_pkg.Group(self.cache, pkg.name)
            assert any(pkg.id == p.id for p in group)

    def test_iteration(self):
        """Check that iteration works correctly."""
        for pkg in self.cache.packages:
            group = apt_pkg.Group(self.cache, pkg.name)

            list(group) == list(group)


if __name__ == "__main__":
    unittest.main()
