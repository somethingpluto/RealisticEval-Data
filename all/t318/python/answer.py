def count_numbers(s: str) -> int:
    number_count = 0
    for char in s:
        if '0' <= char <= '9':
            number_count += 1
    return number_count