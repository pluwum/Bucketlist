from models import Item, BucketList, User
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
        self.assertEqual(1, len(self.exampleBucketList.item_list),
                         msg="The item was not deleted")

    def test_for_editing_item(self):
        name = 'Mexico'
        description = "Am going to Mexico this year."
        self.exampleBucketList.add_bucket_list_item(name, description)
        result = self.exampleBucketList.edit_bucket_list_item('Mexico', 'Travel',
                                                              'We should travel the world')
        self.assertEqual('We should travel the world', result.description,
                         msg="The item is not being edited.")


class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.example_user = User('Brian', 'Serumaga', 'bsk20111@hotmail.com', 'pumpkin')

    def test_for_adding_bucketlist(self):
        self.example_user.add_new_bucket_list("Growth")
        self.assertEqual(len(self.example_user.bucket_lists), 1,
                         msg="New Bucket list has been added.")


if __name__ == '__main__':
    unittest.main()
