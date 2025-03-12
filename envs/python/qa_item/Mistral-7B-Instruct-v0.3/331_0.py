import re
from decimal import Decimal

def calculate_final_price(price: str, discount: str) -> float:
    """
    Calculates the final price after applying a discount to the original price.
    Both price and discount are expected as strings and should represent valid numbers.
    The discount should be a percentage value between 0 and 100.

    Args:
        price (str): The original price as a string.
        discount (str): The discount percentage as a string.

    Returns:
        float: The final price after applying the discount, rounded to two decimal places.

    Raises:
        ValueError: Will throw an error if price or discount aren't valid numbers or if the discount is out of the expected range.
    """

    # Validate price
    if not re.match(r'^\d+(\.\d{1,2})?$', price):
        raise ValueError("Invalid price format. Expected a number with optional decimal points.")

    # Convert price to Decimal
    price = Decimal(price)

    # Validate discount
    if not re.match(r'^\d+$', discount):
        raise ValueError("Invalid discount format. Expected an integer representing the discount percentage.")

    # Convert discount to Decimal and normalize to a percentage
    discount = Decimal(discount) / 100

    # Calculate final price
    final_price = price * (1 - discount)

    # Round final price to two decimal places
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