import random

def shuffle(array):
    current_index = len(array)
    while current_index > 0:
        random_index = random.randint(0, current_index - 1)  # Get a random index
        current_index -= 1
        # Swap the elements at current_index and random_index
        array[current_index], array[random_index] = array[random_index], array[current_index]
    return array