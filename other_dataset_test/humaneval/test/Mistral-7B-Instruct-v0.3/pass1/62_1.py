

METADATA = {}


def check(candidate):
    assert candidate([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
    assert candidate([1, 2, 3]) == [2, 6]
    assert candidate([3, 2, 1]) == [2, 2]
    assert candidate([3, 2, 1, 0, 4]) == [2, 2, 0, 16]
    assert candidate([1]) == []

def derivative(xs):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
     Return derivative of this polynomial in the same form.
    """
    result = []
    for i in range(1, len(xs)):
        result.append(i * xs[i])
    result.append(0) # add 0 for the constant term
    for i in range(len(xs) - 2, -1, -1):
        result[i] += (len(xs) - i) * xs[i]
    return result
candidate = derivative
check(candidate)