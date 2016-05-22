"""
Checkout class.
"""
from pykata09 import settings


class CheckOut:
    def __init__(self, rules=None):
        self._total = 0
        self._items = []
        self.rules = rules

    def scan(self, item):
        try:
            self._total += settings.PRICE_LIST[item]
        except KeyError:
            raise ValueError("Sorry, we don't sell that item here.")
        else:
            self._items.append(item)

    def total(self):
        if self.rules is None:
            return self._total
        return self.check_rules()

    def check_rules(self):
        discount = 0
        for rule in self.rules:
            discount += rule(self._items)
        return self._total - discount
