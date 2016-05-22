"""
Promotional Rules.
"""


def basic_promo(items, item, reduction, num_items):
    reduction_amount = reduction
    item_count = items.count(item)
    num_of_promos_to_apply = item_count // num_items
    discount = num_of_promos_to_apply * reduction_amount
    return discount


def apples_promo_discount(items):
    return basic_promo(items, item='A', reduction=20, num_items=3)


def bananas_promo_discount(items):
    return basic_promo(items, item='B', reduction=15, num_items=2)
