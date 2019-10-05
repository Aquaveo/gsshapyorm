import unittest
from gsshapyorm.util import import_optional


def optional_installed(a, b, c):
    os_path = import_optional('os.path', optional_installed)
    return os_path.join(c, a, b)


def optional_not_installed(a, b, c=''):
    os_path = import_optional('not__a__package', optional_installed)
    return os_path.join(c, a, b)


class TestUtilityMethods(unittest.TestCase):
    pass

    def test_import_optional(self):
        ret = optional_installed('foo', 'bar', 'goo')
        self.assertEqual('goo/foo/bar', ret)

    def test_import_optional_not_installed(self):
        with self.assertRaises(ModuleNotFoundError) as cm:
            optional_not_installed('foo', 'bar', 'goo')

        self.assertEqual('Please install optional dependency "not__a__package" '
                         'to use function/method "optional_installed()".', str(cm.exception))
