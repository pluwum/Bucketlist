import unittest
from ..classes.item import Item


class ItemTestCases(unittest.TestCase):

    def setUp(self):
        name = "Go to Bahamas"
        description = "To go to the Bahamas to see what's up."
        self.item1 = Item(name, description)

    def test_for_default_progress(self):
        self.assertFalse(self.item1.progress, msg="The default progress is wrong.")