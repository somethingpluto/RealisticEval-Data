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
    try:
        price_value = float(price)
        discount_value = float(discount)
    except ValueError:
        raise ValueError("Both price and discount must be valid numbers.")

    if not (0 <= discount_value <= 100):
        raise ValueError("Discount must be a percentage value between 0 and 100.")

    final_price = price_value * (1 - discount_value / 100)
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