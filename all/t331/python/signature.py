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