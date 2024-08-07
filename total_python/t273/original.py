'''
    Written by ChatGPT
    divides up a list to num_parts parts
    @lst: a list to be divided
    @num_parts: integer. number of parts you want to divide lst to
    @return: a list of lists that are parts of the input lst
'''
def divide_list(lst, num_parts):
    avg = len(lst) // num_parts
    remainder = len(lst) % num_parts
    result = []

    i = 0
    for _ in range(num_parts):
        part_size = avg + 1 if remainder > 0 else avg
        result.append(lst[i:i + part_size])
        i += part_size
        remainder -= 1

    return result