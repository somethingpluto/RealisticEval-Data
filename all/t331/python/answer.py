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
        ValueError: If price or discount aren't valid numbers or if the discount is out of the expected range.
    """
    try:
        price_value = float(price)
        discount_value = float(discount)
    except ValueError:
        raise ValueError('Invalid price or discount value.')

    if discount_value < 0 or discount_value > 100:
        raise ValueError('Discount percentage must be between 0 and 100.')

    discount_amount = price_value * discount_value / 100
    final_price = price_value - discount_amount

    return round(final_price, 2)
