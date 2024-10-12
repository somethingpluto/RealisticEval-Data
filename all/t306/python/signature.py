def get_price(recipe_id: str, min_val: float = 10, max_val: float = 30) -> float:
    """
    The recipe ID is hashed to produce a price in the specified range.

    :param recipe_id: The ID of the recipe to hash.
    :param min_val: The minimum value of the price range (default is 10).
    :param max_val: The maximum value of the price range (default is 30).
    :returns: The hashed price, mapped to the specified range with two decimal places.
    """