import datetime
import unittest
import json
import os

from pyubibot import Channel


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        with open(os.path.join(os.path.join(os.path.dirname(__file__),"testchannel.json"))) as json_file:
            self.channel = Channel(json.load(json_file), 1234)

    def test_get_field_name_by_sensor(self):
        self.assertEqual(self.channel.get_field_name_by_sensor("Temperature"), "field1")
        self.assertEqual(self.channel.get_field_name_by_sensor("Humidity"), "field2")
        self.assertEqual(self.channel.get_field_name_by_sensor("Light"), "field3")

    def test_get_last_value(self):
        self.assertTrue(self.channel.get_last_value() is not None)

    def test_get_last_value_by_field(self):
        self.assertEqual(self.channel.get_last_value_by_field("field1"), 35.806824)
        self.assertEqual(self.channel.get_last_value_by_field("field2"), 20)
        self.assertEqual(self.channel.get_last_value_by_field("field3"), 0)

    def test_get_last_updated_by_field(self):
        self.assertAlmostEqual(self.channel.get_last_updated_by_field("field1"),
                               datetime.datetime.strptime("2020-02-24T20:52:38Z", "%Y-%m-%dT%H:%M:%SZ"))
        self.assertAlmostEqual(self.channel.get_last_updated_by_field("field2"),
                               datetime.datetime.strptime("2020-02-24T20:52:38Z", "%Y-%m-%dT%H:%M:%SZ"))
        self.assertAlmostEqual(self.channel.get_last_updated_by_field("field3"),
                               datetime.datetime.strptime("2020-02-24T20:52:38Z", "%Y-%m-%dT%H:%M:%SZ"))


if __name__ == '__main__':
    unittest.main()
