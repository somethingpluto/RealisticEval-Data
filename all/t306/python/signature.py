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