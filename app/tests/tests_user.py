"""Module containing the User Class tests"""
from ..bucketlist.user import User
import unittest


class UserTestCase(unittest.TestCase):
    """Class containing the user TestCases"""
    def setUp(self):
        self.example_user = User('Brian', 'Serumaga', 'bsk20111@hotmail.com', 'pumpkin')
        self.example_user.add_new_bucket_list("Programming")

    def test_for_adding_bucketlist(self):
        """Test for adding a new bucket list"""
        self.example_user.add_new_bucket_list("Growth")
        self.assertEqual(len(self.example_user.bucket_lists), 2,
                         msg="New Bucket list has been added.")

    def test_view_bucketlist(self):
        """Test for viewing a bucket list"""
        example1 = self.example_user.view_bucket_list('Programming')
        self.assertEqual(example1.name, 'Programming', msg="Unable to view the bucket list")

    def test_editing_bucket_list(self):
        """Test for editing a bucket list"""
        result = self.example_user.edit_bucket_list('Programming', 'Agriculture')
        self.assertEqual(result.name, 'Agriculture', msg="The bucket list was not edited")

    def test_delete_bucket_list(self):
        """Test for deleting the bucket list"""
        self.example_user.delete_bucket_list('Programming')
        self.assertEqual(len(self.example_user.bucket_lists), 0, msg="The bucket list was not deleted.")