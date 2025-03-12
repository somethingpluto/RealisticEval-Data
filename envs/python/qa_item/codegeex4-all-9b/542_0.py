def calculate_discount(original_price: float, actual_price: float) -> float:
    """
    Calculates the discount percentage based on the given price and the actual price paid.

    Args:
        original_price (float): The original price of the item.
        actual_price (float): The actual price paid for the item.

    Returns:
        float: The discount percentage, rounded to two decimal places.
    """
    discount = (original_price - actual_price) / original_price
    return round(discount * 100, 2)
import unittest


class TestCalculateDiscount(unittest.TestCase):

    def test_discount_25_percent(self):
        self.assertEqual(calculate_discount(100, 75), 25.00)

    def test_discount_0_percent(self):
        self.assertEqual(calculate_discount(50, 50), 0.00)

    def test_discount_100_percent(self):
        self.assertEqual(calculate_discount(100, 0), 100.00)

    def test_discount_50_percent(self):
        self.assertEqual(calculate_discount(200, 100), 50.00)

if __name__ == '__main__':
    unittest.main()