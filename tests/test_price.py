import unittest

from pykata09.checkout import CheckOut
from pykata09.rules import apples_promo_discount, bananas_promo_discount


RULES = [apples_promo_discount, bananas_promo_discount]


class TestPrice(unittest.TestCase):
    @staticmethod
    def price(goods):
        co = CheckOut(rules=RULES)
        for good in goods:
            co.scan(good)
        return co.total()

    def test_totals_empty(self):
        self.assertEqual(0, self.price(""))

    def test_incorrect_item(self):
        with self.assertRaises(ValueError):
            self.price("Z")

    def test_totals_no_rules(self):
        self.assertEqual(50, self.price("A"))
        self.assertEqual(80, self.price("AB"))
        self.assertEqual(115, self.price("CDBA"))

    def test_totals_with_rules(self):
        self.assertEqual(100, self.price("AA"))
        self.assertEqual(130, self.price("AAA"))
        self.assertEqual(180, self.price("AAAA"))
        self.assertEqual(230, self.price("AAAAA"))
        self.assertEqual(260, self.price("AAAAAA"))

    def test_totals_with_rules_and_others(self):
        self.assertEqual(160, self.price("AAAB"))
        self.assertEqual(175, self.price("AAABB"))
        self.assertEqual(190, self.price("AAABBD"))
        self.assertEqual(190, self.price("DABABA"))

    def test_incremental(self):
        co = CheckOut(rules=RULES)
        self.assertEqual(0, co.total())
        co.scan("A")
        self.assertEqual(50, co.total())
        co.scan("B")
        self.assertEqual(80, co.total())
        co.scan("A")
        self.assertEqual(130, co.total())
        co.scan("A")
        self.assertEqual(160, co.total())
        co.scan("B")
        self.assertEqual(175, co.total())
