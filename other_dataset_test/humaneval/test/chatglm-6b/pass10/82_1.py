def check(candidate):

    # Check some simple cases
    assert candidate('Hello') == True
    assert candidate('abcdcba') == True
    assert candidate('kittens') == True
    assert candidate('orange') == False
    assert candidate('wow') == True
    assert candidate('world') == True
    assert candidate('MadaM') == True
    assert candidate('Wow') == True
    assert candidate('') == False
    assert candidate('HI') == True
    assert candidate('go') == True
    assert candidate('gogo') == False
    assert candidate('aaaaaaaaaaaaaaa') == False

    # Check some edge cases that are easy to work out by hand.
    assert candidate('Madam') == True
    assert candidate('M') == False
    assert candidate('0') == False


def prime_length(string):
    if len(string) <= 1:
        return False

    primes = []
    for i in range(len(string)):
        if string[i] % 2 == 0:
            primes.append(i)
        else:
            if i > 2:
                if prime_length(string[:i]) and prime_length(string[i+1:]):
                    return True
                primes.append(i)

    return False

candidate = prime_length
check(candidate)