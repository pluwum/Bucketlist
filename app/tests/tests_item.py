"""Module containing the TestCase for Item Class"""
import unittest
from ..bucketlist.item import Item


class ItemTestCases(unittest.TestCase):
    """Class for the item TestCases"""
    def setUp(self):
        name = "Go to Bahamas"
        description = "To go to the Bahamas to see what's up."
        self.item1 = Item(name, description)

    def test_for_default_progress(self):
        """Test to check for the default progress"""
        self.assertFalse(self.item1.progress, msg="The default progress is wrong.")
