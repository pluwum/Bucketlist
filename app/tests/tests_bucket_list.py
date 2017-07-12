"""Module containing the testcases for the bucket list."""
import unittest
from ..bucketlist.bucket_list import BucketList


class BucketListTestCase(unittest.TestCase):
    """Class containing the testcases for bucket list."""
    def setUp(self):
        self.exampleBucketList = BucketList('Africa')
        self.exampleBucketList.add_bucket_list_item('Tokyo', "Am going to Tokyo this year.")

    def test_BucketList_class(self):
        """Test for attribute of bucket list (name)"""
        self.assertEqual(type(self.exampleBucketList.name), str,
                         msg="The class doesn't exist")

    def test_for_adding_item(self):
        """Test for adding a new bucket list item"""
        self.exampleBucketList.add_bucket_list_item('Read', "Reading is important")
        self.assertEqual(len(self.exampleBucketList.item_list), 2,
                         msg="The item is not being added properly")

    def test_for_viewing_item(self):
        """Test for viewing a bucket list item"""
        example = self.exampleBucketList.view_bucket_list_item("Tokyo")
        self.assertEqual(example.description, "Am going to Tokyo this year.",
                         msg="Returning the wrong result")

    def test_for_deleting_item(self):
        """Test for deleting a bucket list item"""
        self.exampleBucketList.add_bucket_list_item('China', "Am going to China this year.")
        self.exampleBucketList.delete_bucket_list_item("China")
        self.assertEqual(len(self.exampleBucketList.item_list), 1,
                         msg="The item was not deleted")


