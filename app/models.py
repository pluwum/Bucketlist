class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.progress = False


class BucketList(object):
    item_list = []

    def __init__(self, name):
        self.name = name

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