import random
import string

def generate_random_string() -> str:
    """Generates a random string of length 25 containing both upper case (A-Z) and lower case (a-z) letters.

    Returns:
        str: A randomly generated string that meets the criteria of including both upper and lower case letters.
    """
    # Define the character pool with upper and lower case letters
    characters = string.ascii_letters  # This includes both a-z and A-Z

    # Generate a random string of length 25
    random_string = ''.join(random.choice(characters) for _ in range(25))

    return random_string