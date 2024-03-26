import unittest
from working_with_yaml_files import parse_yaml

class TestParseYaml(unittest.TestCase):
    def test_parse_yaml(self):
        self.assertIsInstance(parse_yaml("C:/py_files/interface.yaml"), dict)
        self.assertEqual(parse_yaml("C:/py_files/interface.yaml")["interface"]["name"], "GigabitEthernet1")