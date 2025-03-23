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
    # Check if the number is less than 100
    if a < 100:
        # Make sure the number is prime
        if a % 2 == 0 or a % 3 == 0 or a % 5 == 0 or a % 7 == 0:
            return False
        # Find the factors of the number
        for i in range(2, int(a ** 0.5) + 1):
            if a % i == 0:
                return False
        # Check if the multiplication of the prime factors is equal to the number
        for i in range(2, int(a ** 0.5) + 1):
            for j in range(3, int(a ** 0.5) + 1):
                for k in range(5, int(a ** 0.5) + 1):
                    if i * j * k == a:
                        return False
        return True
    else:
        return False

>>> is_multiply_prime(30)
True

>>> is_multiply_prime(2 * 3 * 5)
False

>>> is_multiply_prime(100)
False

candidate = is_multiply_prime
check(candidate)