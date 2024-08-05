import unittest

from total.t6.adapted import get_name


class TestGetName(unittest.TestCase):
    def test_get_name_case1(self):
        self.assertEqual(get_name("/artifacts/bundle/items/workspace/properties_include"), "workspace")

    def test_get_name_case2(self):
        self.assertEqual(get_name("/resources/items/environment/"), "environment")

    def test_get_name_case3(self):
        self.assertEqual(get_name("items/artifacts/"), "")

    def test_get_name_case4(self):
        self.assertEqual(get_name("/environments/bundle_items"), "bundle")

    def test_get_name_case5(self):
        self.assertEqual(get_name("/include/environments_artifacts/items_properties"), "environments_artifacts")
