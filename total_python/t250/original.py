from collections import defaultdict

import distinctipy


def reverse_dict(input_dict):
    reversed_dict = defaultdict(list)
    for key, value in input_dict.items():
        reversed_dict[value].append(key)
    return dict(reversed_dict)
