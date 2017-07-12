"""Module containing the TestCases for the Bucket List Class"""
import unittest
from ..bucketlist.bucket_list_app import BucketListApp


class BucketListAppTestcases(unittest.TestCase):
    """Class containing the bucket list app TestCases"""
    def setUp(self):
        self.example1 = BucketListApp()
        self.example1.add_user('Nelson', 'Kiggundu', 'Nking@hotmail.com', '123456')

    def test_for_adding_users(self):
        """Test for adding a user functionality"""
        self.example1.add_user('Brian', 'Serumaga', 'bsk2012@hotmail.com', '12345')
        self.assertEqual(len(self.example1.list_of_users), 2, msg="The user wasn't added")

    def test_for_login_user(self):
        """Test for login in user function"""
        self.example1.login_user('Nking@hotmail.com', '123456')
        self.assertEqual(self.example1.current_user.email, 'Nking@hotmail.com',
                         msg="The user was unable to login.")

    def test_for_invalid_login_user(self):
        """Test for login in user function"""
        self.assertEqual(self.example1.login_user('Nking@hotmail.com', '123'),
                         'Invalid Login Details', msg="The user was unable to login.")

    def test_for_user_sign_out(self):
        """Test for when user signs out"""
        self.example1.sign_out()
        self.assertIsNone(self.example1.current_user,
                          msg=" The person wasn't logged out successfully")
