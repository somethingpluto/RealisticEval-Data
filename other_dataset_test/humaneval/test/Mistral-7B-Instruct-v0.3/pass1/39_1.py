

METADATA = {}


def check(candidate):
    assert candidate(1) == 2
    assert candidate(2) == 3
    assert candidate(3) == 5
    assert candidate(4) == 13
    assert candidate(5) == 89
    assert candidate(6) == 233
    assert candidate(7) == 1597
    assert candidate(8) == 28657
    assert candidate(9) == 514229
    assert candidate(10) == 433494437

def fibonacci(n: int):
    """
    fibonacci returns the n-th Fibonacci number.
    """
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n - 1]

def is_prime(n: int):
    """
    is_prime checks if n is a prime number.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    fib_num = 1
    fib = [0, 1]
    while len(fib) < n:
        fib_num = fib[len(fib) - 1] + fib[len(fib) - 2]
        if is_prime(fib_num):
            fib.append(fib_num)
            if len(fib) == n:
                return fib_num

    # If n is larger than the largest Fibonacci prime number found, return None
    return None
candidate = prime_fib
check(candidate)