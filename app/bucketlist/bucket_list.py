"""Module containing the Bucket List Class"""
from ..bucketlist.item import Item


class BucketList(object):
    """Class containing the Bucket List methods"""
    def __init__(self, name):
        self.name = name
        self.item_list = []

    def add_bucket_list_item(self, item_name, description):
        item1 = Item(item_name, description)
        self.item_list.append(item1)

    def view_bucket_list_item(self, name):
        for obj in self.item_list:
            if obj.name == name:
                return obj

    def edit_bucket_list_item(self):
        pass

    def delete_bucket_list_item(self, name):
        for obj in self.item_list:
            if obj.name == name:
                self.item_list.remove(obj)