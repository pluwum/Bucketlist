from models import Item, BucketList
import unittest


class ItemTestCases(unittest.TestCase):
    def setUp(self):
        name = "Go to Bahamas"
        description = "To go to the Bahamas to see what's up."
        self.item1 = Item(name, description)

    def test_for_default_progress(self):
        self.assertFalse(self.item1.progress, msg="The default progress is wrong.")


class BucketListTestCase(unittest.TestCase):
    def setUp(self):
        self.exampleBucketList = BucketList('Africa')

    def test_BucketList_class(self):
        self.assertEqual(type(self.exampleBucketList.name), str,
                         msg="The class doesn't exist")

    def test_for_adding_item(self):
        name= 'Tokyo'
        description = "Am going to Tokyo this year."
        self.exampleBucketList.add_bucket_list_item(name, description)
        self.assertEqual(len(self.exampleBucketList.item_list), 1,
                         msg="The item is not being added properly")

    def test_for_viewing_item(self):
        example = self.exampleBucketList.view_bucket_list_item("Tokyo")
        self.assertEqual(example.description, "Am going to Tokyo this year.",
                         msg="Returning the wrong result")

    def test_for_deleting_item(self):
        name = 'China'
        description = "Am going to China this year."
        self.exampleBucketList.add_bucket_list_item(name, description)
        self.exampleBucketList.delete_bucket_list_item("China")
        self.assertEqual(len(self.exampleBucketList.item_list), 1,
                         msg="The item was not deleted")


