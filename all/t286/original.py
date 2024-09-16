def find_nice_number(n):
    # Written by ChatGPT
    half_n = n / 2
    # Check for numbers divisible by 10
    for i in range(int(n), int(half_n) - 1, -1):
        if i % 10 == 0:
            return i
    # If no number divisible by 10, check for numbers divisible by 5
    for i in range(int(n), int(half_n) - 1, -1):
        if i % 5 == 0:
            return i
    # Return None if no such number found
    return 10
