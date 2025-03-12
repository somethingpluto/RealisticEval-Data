import hashlib

def get_price(recipe_id: str, min_val: float = 10, max_val: float = 30) -> float:
    """
    The recipe ID is hashed to produce a price in the specified range.
    Args:
        recipe_id (str): The ID of the recipe to hash.
        min_val (float): The minimum value of the price range (default is 10).
        max_val (float): The maximum value of the price range (default is 30).

    Returns:
        float: The hashed price, mapped to the specified range with two decimal places.
    """

    hash_object = hashlib.md5(recipe_id.encode())
    hashed_value = int(hash_object.hexdigest(), 16)

    price_range = max_val - min_val
    normalized_value = min_val + (hashed_value % 1000) / 1000 * price_range

    return round(normalized_value, 2)
import unittest


class TestGetPrice(unittest.TestCase):

    def test_default_range(self):
        price = get_price('recipe123')
        self.assertGreaterEqual(price, 10)
        self.assertLessEqual(price, 30)

    def test_same_price_for_same_id(self):
        price1 = get_price('recipe123')
        price2 = get_price('recipe123')
        self.assertEqual(price1, price2)

    def test_different_prices_for_different_ids(self):
        price1 = get_price('recipe123')
        price2 = get_price('recipe456')
        self.assertNotEqual(price1, price2)

    def test_custom_range(self):
        min_val = 20
        max_val = 50
        price = get_price('recipe789', min_val, max_val)
        self.assertGreaterEqual(price, min_val)
        self.assertLessEqual(price, max_val)

    def test_long_recipe_id(self):
        long_recipe_id = 'recipe' + 'A' * 1000
        price = get_price(long_recipe_id)
        self.assertGreaterEqual(price, 10)
        self.assertLessEqual(price, 30)

if __name__ == '__main__':
    unittest.main()