def find_primes(lower_bound, upper_bound):
    prime_numbers = []
    for number in range(lower_bound, upper_bound + 1):
        if is_prime(number):
            prime_numbers.append(number)
    return prime_numbers


def compute_sum_of_primes(primes):
    total = sum(primes)
    return total


def is_prime(num):
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True
