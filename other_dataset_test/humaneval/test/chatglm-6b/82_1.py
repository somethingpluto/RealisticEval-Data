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
            primes.append(True)
        else:
            if string[i] == string[i + 1]:
                continue
            else:
                primes.append(False)
    
    return all(primes)

string = 'Hello'
print(prime_length(string))  # True

string = 'abcdcba'
print(prime_length(string))  # True

string = 'kittens'
print(prime_length(string))  # True

string = 'orange'
print(prime_length(string))  # False

candidate = prime_length
check(candidate)