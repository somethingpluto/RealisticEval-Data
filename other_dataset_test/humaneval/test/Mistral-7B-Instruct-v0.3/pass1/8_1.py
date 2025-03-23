

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([]) == (0, 1)
    assert candidate([1, 1, 1]) == (3, 1)
    assert candidate([100, 0]) == (100, 0)
    assert candidate([3, 5, 7]) == (3 + 5 + 7, 3 * 5 * 7)
    assert candidate([10]) == (10, 10)
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)

    sum_ = 0
    product_ = 1
    for number in numbers:
        sum_ += number
        product_ *= number

    return (sum_, product_)
candidate = sum_product
check(candidate)