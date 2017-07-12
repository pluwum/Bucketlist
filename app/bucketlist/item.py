"""Module containing item class"""


class Item(object):
    """Class used to store bucket list item properties"""
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.progress = False