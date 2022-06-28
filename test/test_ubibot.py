import unittest

from unittest.mock import MagicMock
from pyubibot import Ubibot

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.ubibot = Ubibot("123abc")
        self.ubibot.get_channel = MagicMock(return_value={})
        self.ubibot.get_channels = MagicMock(return_value={})
    
    def test_get_channel(self):
        assert self.ubibot.get_channel() == {}
    
    def test_get_channels(self):
        assert self.ubibot.get_channels() == {}

if __name__ == '__main__':
    unittest.main()