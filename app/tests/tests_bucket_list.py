"""Module containing the testcases for the bucket list."""
import unittest
from ..bucketlist.bucket_list import BucketList


class BucketListTestCase(unittest.TestCase):
    """Class containing the testcases for bucket list."""
    def setUp(self):
        self.example_bucket_list = BucketList('Africa')
        self.example_bucket_list.add_bucket_list_item('Tokyo', "Am going to Tokyo this year.")

    def test_bucket_list_class(self):
        """Test for attribute of bucket list (name)"""
        self.assertEqual(type(self.example_bucket_list.name), str,
                         msg="The class doesn't exist")

    def test_for_adding_item(self):
        """Test for adding a new bucket list item"""
        self.example_bucket_list.add_bucket_list_item('Read', "Reading is important")
        self.assertEqual(len(self.example_bucket_list.item_list), 2,
                         msg="The item is not being added properly")

    def test_for_viewing_item(self):
        """Test for viewing a bucket list item"""
        example = self.example_bucket_list.view_bucket_list_item("Tokyo")
        self.assertEqual(example.description, "Am going to Tokyo this year.",
                         msg="Returning the wrong result")

    def test_for_deleting_item(self):
        """Test for deleting a bucket list item"""
        self.example_bucket_list.add_bucket_list_item('China', "Am going to China this year.")
        self.example_bucket_list.delete_bucket_list_item("China")
        self.assertEqual(len(self.example_bucket_list.item_list), 1,
                         msg="The item was not deleted")

    def test_for_editing_item(self):
        """Tests for editing an item"""
        result = self.example_bucket_list.edit_bucket_list_item('Tokyo', 'Travelling',
                                                                'Travel to open up your mind', True)
        self.assertEqual('Travelling', result.name, msg="The item name wasn't changed")
        self.assertEqual('Travel to open up your mind', result.description,
                         msg="The item description wasn't changed")
