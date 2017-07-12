class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.progress = False


class BucketList(object):

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

    def edit_bucket_list_item(self, item_name, new_name, new_description):
        for obj in self.item_list:
            if obj.name == item_name:
                obj.name = new_name
                obj.description = new_description
                return obj

    def delete_bucket_list_item(self, name):
        for obj in self.item_list:
            if obj.name == name:
                self.item_list.remove(obj)


class User(object):

    def __init__(self, fname, sname, email, password):
        self.fname = fname
        self.sname = sname
        self.email = email
        self.password = password
        self.bucket_lists = []

    def add_new_bucket_list(self,bucket_list_name):
        new_bucket_list = BucketList(bucket_list_name)
        self.bucket_lists.append(new_bucket_list)

    def view_bucket_list(self, bucket_name):
        for obj in self.bucket_lists:
            if obj.name == bucket_name:
                return obj
