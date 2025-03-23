

METADATA = {}


def check(candidate):
    import math
    import random
    rng = random.Random(42)
    import copy
    for _ in range(100):
        ncoeff = 2 * rng.randint(1, 4)
        coeffs = []
        for _ in range(ncoeff):
            coeff = rng.randint(-10, 10)
            if coeff == 0:
                coeff = 1
            coeffs.append(coeff)
        solution = candidate(copy.deepcopy(coeffs))
        assert math.fabs(poly(coeffs, solution)) < 1e-4

scss
def find_zero(xs: list):
    """
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    
    Example:
    find_zero([1, 2], 2) # f(x) = 1 + 2x
    find_zero([-6, 11, -6, 1], 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    find_zero([-2, -1, 2, 1], 2) # -2 + -1x + 2x^2 + x^3 = -2 - x^2 - x
    """
    if len(xs) % 2 == 0:
        x = max(xs)
    else:
        x = min(xs)
    return x

candidate = find_zero
check(candidate)