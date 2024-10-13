import random


def generate_random_string(cls):
    # Use a list to construct the random string
    random_string = []

    # Ensure at least one upper case and one lower case letter
    random_string.append(random.choice(cls.LOWER_CASE))
    random_string.append(random.choice(cls.UPPER_CASE))

    # Fill the rest of the string length with random characters
    all_characters = cls.LOWER_CASE + cls.UPPER_CASE
    for _ in range(2, cls.LENGTH):
        random_char = random.choice(all_characters)
        random_string.append(random_char)

    # Shuffle the characters to ensure randomness
    return cls.shuffle_string(''.join(random_string))