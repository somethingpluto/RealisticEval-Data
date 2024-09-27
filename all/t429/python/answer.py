def count_contained_ranges(file_path):
    """
    Reads a file containing ranges and counts how many ranges fully contain each other.

    Args:
        file_path (str): The path to the input file containing ranges in the format 'start-end'.

    Returns:
        int: The count of pairs where one range fully contains another.
    """
    ranges = []

    # Read input and create a list of ranges
    with open(file_path, 'r') as input_file:
        for line in input_file:
            print(line.strip())  # Print the line (removing any extra whitespace)
            start, end = map(int, line.strip().split('-'))  # Parse start and end
            ranges.append((start, end))  # Append the tuple to the ranges list

    # Initialize counter
    counter = 0

    # Iterate over each pair of ranges
    for i in range(len(ranges)):
        for j in range(len(ranges)):
            if i != j:  # Avoid comparing the same range
                r1 = ranges[i]
                r2 = ranges[j]

                # Check if r1 fully contains r2 or vice versa
                if (r1[0] <= r2[0] and r1[1] >= r2[1]) or (r2[0] <= r1[0] and r2[1] >= r1[1]):
                    counter += 1

    return counter