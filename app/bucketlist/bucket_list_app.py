"""Module for the Bucket List App"""
from ..bucketlist.user import User


class BucketListApp(object):
    def __init__(self):
        self.current_user = None
        self.list_of_users = []

    def add_user(self):
        pass