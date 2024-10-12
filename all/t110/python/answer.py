import random
import string


def generate_uuid() -> str:
    """
    Generate a random UUID of length 36.
    The UUID contains at least one uppercase letter, one lowercase letter, and one digit.

    Returns:
        str: A 36-character UUID string.
    """
    # Define the characters that can appear in the UUID
    possible_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits

    # Initialize an empty list to build the UUID
    uuid = []

    # Generate 36 characters for the UUID
    for _ in range(36):
        uuid.append(random.choice(possible_chars))

    # Ensure at least one uppercase letter, one lowercase letter, and one digit
    uuid[0] = random.choice(string.ascii_uppercase)  # Ensure at least one uppercase letter
    uuid[1] = random.choice(string.ascii_lowercase)  # Ensure at least one lowercase letter
    uuid[2] = random.choice(string.digits)  # Ensure at least one digit

    # Shuffle the UUID to randomize the positions
    random.shuffle(uuid)

    # Return the generated UUID as a string
    return ''.join(uuid)