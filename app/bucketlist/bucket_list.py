"""Module containing the Bucket List Class"""
from ..bucketlist.item import Item


class BucketList(object):
    """Class containing the Bucket List methods"""
    def __init__(self, name):
        self.name = name
        self.item_list = []
        self.progress = False

    def add_bucket_list_item(self, item_name, description):
        """
        Method for adding a new bucket list item
        params: item_name , description
        """
        item1 = Item(item_name, description)
        self.item_list.append(item1)

    def view_bucket_list_item(self, name):
        """
        Method for viewing a bucket list item.
        :params: name
        return: object
        """
        for obj in self.item_list:
            if obj.name == name:
                return obj

    def edit_bucket_list_item(self, item_name , new_name, new_description, new_progress=False):
        """
        Method for editing a bucket list item
        params: item_name , new_name, new_description, new_progress
        """
        for obj in self.item_list:
            if obj.name == item_name:
                obj.name = new_name
                obj.description = new_description
                obj.progress = new_progress

    def delete_bucket_list_item(self, name):
        """
        Method for deleting a bucket list item
        params: name
        """
        for obj in self.item_list:
            if obj.name == name:
                self.item_list.remove(obj)
