"""Module for the Bucket List App"""
from ..bucketlist.user import User


class BucketListApp(object):
    """Class containing the bucket list methods"""
    def __init__(self):
        self.current_user = None
        self.list_of_users = []

    def add_user(self, fname, lname, email, password):
        """Method for adding a user"""
        new_user = User(fname, lname, email, password)
        self.list_of_users.append(new_user)

    def login_user(self, email, password):
        """Method for user login"""
        for obj in self.list_of_users:
            if obj.email == email and obj.password == password:
                self.current_user = obj
            return 'Invalid Login Details'

    def sign_out(self):
        """Method for  signing out a user"""
        self.current_user = None