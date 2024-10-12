def calculate_discount(original_price: float, actual_price: float) -> float:
    """
    Calculates the discount percentage based on the given price and the actual price paid.

    :param original_price: The original price of the item.
    :param actual_price: The actual price paid for the item.
    :return: The discount percentage, rounded to two decimal places.
    """
    # Validate input
    if original_price <= 0:
        raise ValueError('Original price must be greater than zero.')
    if actual_price < 0:
        raise ValueError('Actual price cannot be negative.')

    # Calculate the discount
    discount_amount = original_price - actual_price
    discount_percentage = (discount_amount / original_price) * 100

    # Return the discount percentage, rounded to two decimal places
    return round(discount_percentage, 2)
