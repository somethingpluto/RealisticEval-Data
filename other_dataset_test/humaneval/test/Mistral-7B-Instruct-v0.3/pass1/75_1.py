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

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_multiply_prime(a):
    if a < 2:
        return False
    if a == 2:
        return True
    if a % 2 == 0:
        return False
    if a % 3 == 0:
        return False
    if a % 5 == 0:
        return False
    for i in range(5, int(a**0.5) + 1, 6):
        if a % i == 0 or a % (i + 2) == 0 or a % (i + 4) == 0:
            return False
    return True
candidate = is_multiply_prime
check(candidate)