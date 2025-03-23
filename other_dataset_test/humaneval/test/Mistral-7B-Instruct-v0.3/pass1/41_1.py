

METADATA = {}


def check(candidate):
    assert candidate(2) == 4
    assert candidate(3) == 9
    assert candidate(4) == 16
    assert candidate(8) == 64
    assert candidate(10) == 100

def car_race_collision(n):
    # The speed of each car is assumed to be 1 unit per time step
    # The midpoint of the cars' paths is the average of their positions
    # Collisions occur when the midpoint is an integer

    # Initialize the positions of the cars moving left to right and right to left
    left_positions = list(range(n))
    right_positions = list(range(n, 0, -1))

    # Iterate through time steps
    for _ in range(2 * n):
        # Move the cars one step forward
        left_positions = [pos + 1 for pos in left_positions]
        right_positions = [pos - 1 for pos in right_positions]

        # Check for collisions by checking if the midpoint is an integer
        if (sum(left_positions) + sum(right_positions)) / 2 == int((sum(left_positions) + sum(right_positions)) / 2):
            return 1

    # If no collisions occurred, return 0
    return 0
candidate = car_race_collision
check(candidate)