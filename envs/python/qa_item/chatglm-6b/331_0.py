
def calculate_final_price(price: str, discount: str) -> float:
    if not price or not discount or price.isdigit() or discount.isdigit():
        raise ValueError("Invalid input values for price and discount.")

    price_percentage = float(price / 100)
    discount_percentage = discount / 100

    final_price = price * (1 + price_percentage) / 100
    final_price = round(final_price, 2)

    return final_price

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