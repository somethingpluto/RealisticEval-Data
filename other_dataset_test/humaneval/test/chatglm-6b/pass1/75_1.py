def check(candidate):

    assert candidate(5) == False
    assert candidate(30) == True
    assert candidate(8) == True
    assert candidate(10) == False
    assert candidate(125) == True
    assert candidate(3 * 5 * 7) == True
    assert candidate(3 * 6 * 7) == False
    assert candidate(9 * 9 * 9) == False
    assert candidate(11 * 9 * 9) == False
    assert candidate(11 * 13 * 7) == True


def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a < 100:
        # Find the three prime numbers
        p1 = 2
        p2 = 3
        p3 = 5

        # Check if the product of these numbers is prime
        if a * p1 * p2 == 1:
            return True
        if a * p1 * p3 == 1:
            return True
        if a * p2 * p3 == 1:
            return True

        # If none of the above conditions are met, the number is not multiply prime
        return False

candidate = is_multiply_prime
check(candidate)