import math

def calculate_final_price(price: str, discount: str) -> float:
    try:
        price = float(price)
        discount = float(discount)
    except ValueError:
        raise ValueError("Price and discount should be valid numbers.")
    
    if discount < 0 or discount > 100:
        raise ValueError("Discount should be a percentage value between 0 and 100.")
    
    final_price = price * (1 - discount / 100)
    return round(final_price, 2)
import unittest


class TestCalculateFinalPrice(unittest.TestCase):

    def test_calculate_final_price_with_valid_inputs(self):
        """
        should calculate the final price correctly with valid inputs
        """
        result = calculate_final_price('200', '10')
        self.assertEqual(result, 180.0)

    def test_discount_is_zero(self):
        """
        should return the original price when the discount is 0%
        """
        result = calculate_final_price('150', '0')
        self.assertEqual(result, 150.0)

    def test_discount_is_hundred(self):
        """
        should return zero when the discount is 100%
        """
        result = calculate_final_price('100', '100')
        self.assertEqual(result, 0.0)

if __name__ == '__main__':
    unittest.main()