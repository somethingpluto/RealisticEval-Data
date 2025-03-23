def check(candidate):


    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1) == 6, "Error"
    assert candidate([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2) == 5, "Error"
    assert candidate([[0,0,0], [0,0,0]], 5) == 0, "Error"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate([[1,1,1,1], [1,1,1,1]], 2) == 4, "Error"
    assert candidate([[1,1,1,1], [1,1,1,1]], 9) == 2, "Error"

def max_fill(grid, capacity):
    rows, cols = len(grid), len(grid[0])
    water = sum(sum(grid))
    if water <= 0 or water % capacity!= 0:
        return -1  # impossible to empty the grid with the given capacity

    times = water // capacity
    for row in grid:
        water_in_row = sum(row)
        if water_in_row > capacity:
            times += math.ceil(water_in_row / capacity) - 1

    return times
candidate = max_fill
check(candidate)