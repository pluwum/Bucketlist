from ..bucketlist.bucket_list import BucketList


class User(object):
    bucket_lists = []

    def __init__(self, fname, sname, email, password):
        self.fname = fname
        self.sname = sname
        self.email = email
        self.password = password

    def add_new_bucket_list(self,bucket_list_name):
        new_bucket_list = BucketList(bucket_list_name)
        self.bucket_lists.append(new_bucket_list)



