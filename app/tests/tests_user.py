from ..classes.user import User
import unittest


class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.example_user = User('Brian', 'Serumaga', 'bsk20111@hotmail.com', 'pumpkin')

    def test_for_adding_bucketlist(self):
        self.example_user.add_new_bucket_list("Growth")
        self.assertEqual(len(self.example_user.bucket_lists), 1,
                         msg="New Bucket list has been added.")

    #def test_view_bucketlist(self):
    #    example1 = self.example_user.view_bucket_list('Growth')
    #    self.assertEqual(example1.name, 'Growth', msg="Unable to view the bucket list")
