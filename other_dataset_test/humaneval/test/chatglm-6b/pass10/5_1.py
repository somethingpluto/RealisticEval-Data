

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([], 7) == []
    assert candidate([5, 6, 3, 2], 8) == [5, 8, 6, 8, 3, 8, 2]
    assert candidate([2, 2, 2], 2) == [2, 2, 2, 2, 2]

import sys

def main(numbers: List[int]) -> None:
    if len(numbers) == 1:
        numbers = [numbers[0]]
    else:
        numbers = [numbers[0], numbers[1:]]

    intersperse(numbers, 4)

if __name__ == '__main__':
    if len(sys.argv)!= 2:
        print("Usage: python intersperse.py <numbers> <delimeter>")
        sys.exit(1)

    main(sys.argv[1])

candidate = intersperse
check(candidate)