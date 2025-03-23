

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

import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero finds x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    """
    if len(xs) % 2!= 0:
        raise ValueError("The number of coefficients must be even.")

    # Ensure the leading coefficient is non-zero
    if xs[0] == 0:
        raise ValueError("The leading coefficient must be non-zero.")

    # Find the square root of the discriminant
    sqrt_discriminant = math.sqrt(discriminant(xs))

    # Calculate the two possible solutions
    sol1 = (-xs[1] - sqrt_discriminant) / (2 * xs[0])
    sol2 = (-xs[1] + sqrt_discriminant) / (2 * xs[0])

    # If the polynomial is quadratic, return both solutions
    if len(xs) == 3:
        return sol1, sol2
    else:
        # If the polynomial is of higher degree, return only the first solution
        return sol1

def discriminant(xs: list):
    """
    Calculates the discriminant of a polynomial with coefficients xs.
    """
    return pow(xs[1], 2) - 4 * xs[0] * poly(xs[2:], 0)
candidate = find_zero
check(candidate)