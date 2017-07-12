"""Module containing the User class"""
from ..bucketlist.bucket_list import BucketList


class User(object):
    """Class containing the user methods"""

    def __init__(self, fname, sname, email, password):
        self.fname = fname
        self.sname = sname
        self.email = email
        self.password = password
        self.bucket_lists = []

    def add_new_bucket_list(self, bucket_list_name):
        """Method for adding new bucketlist"""
        new_bucket_list = BucketList(bucket_list_name)
        self.bucket_lists.append(new_bucket_list)

    def view_bucket_list(self, bucket_list_name):
        """Method for viewing  the bucket list"""
        for obj in self.bucket_lists:
            if obj.name == bucket_list_name:
                return obj

    def edit_bucket_list(self, bucket_list_name, new_bucket_list_name, new_progress = False):
        """Method for editing the bucket list"""
        for obj in self.bucket_lists:
            if obj.name == bucket_list_name:
                obj.name = new_bucket_list_name
                obj.progress = new_progress
                return obj

    def delete_bucket_list(self, bucket_list_name):
        """Method for deleting the bucket list"""
        for obj in self.bucket_lists:
            if obj.name == bucket_list_name:
                self.bucket_lists.remove(obj)


