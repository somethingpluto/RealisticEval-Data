def josephus(n, k):
    """
    Simulates the Josephus problem using a list to represent the circle of people.

    :param n: The number of people in the circle (1 to n).
    :param k: The step count (every k-th person will be eliminated).
    :return: The position of the last person remaining (1-indexed).
    """

    # Step 1: Create a list to represent the people in the circle
    people = list(range(1, n + 1))  # Create a list of people from 1 to n
    index = 0  # Start from the first person

    # Step 2: Eliminate people until only one remains
    while len(people) > 1:
        # Step 3: Find the index of the person to eliminate
        index = (index + k - 1) % len(people)  # -1 to adjust for zero-based index
        eliminated_person = people.pop(index)  # Eliminate that person
        print(f"Eliminated: {eliminated_person}, Remaining: {people}")

    # Step 4: Return the position of the last remaining person
    return people[0]  # The last remaining person
