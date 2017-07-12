import unittest
from ..bucketlist.bucket_list_app import BucketListApp


class BucketListAppTestcases(unittest.TestCase):
    def setUp(self):
        self.example1 = BucketListApp()
