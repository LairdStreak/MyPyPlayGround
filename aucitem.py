"""
Docstring
"""


class AucItem(object): # pylint: disable=too-few-public-methods
    """Class doc str"""

    def __init__(self, itemId, itemName, change, price):
        self.itemid = itemId
        self.itemname = itemName
        self.changenum = change
        self.price = price
