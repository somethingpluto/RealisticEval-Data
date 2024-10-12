def get_price(recipe_id, min_val=10, max_val=30):
    hash_value = 0

    # Generate a hash from the recipe ID
    for char in recipe_id:
        hash_value = (hash_value << 5) - hash_value + ord(char)  # Equivalent to hash * 31 + char

    # Ensure the hash value is a 32-bit integer
    hash_value &= 0xFFFFFFFF

    # Convert the hash to a positive value
    decimal_value = abs(hash_value)

    # Map the decimal value to the specified price range
    mapped_value = (decimal_value % ((max_val - min_val) * 100)) / 100 + min_val

    # Ensure the final value has exactly two decimal places
    final_value = round(mapped_value, 2)

    return final_value
