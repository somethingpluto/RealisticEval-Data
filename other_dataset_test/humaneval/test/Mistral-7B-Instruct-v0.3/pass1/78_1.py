def check(candidate):

    # Check some simple cases
    assert candidate("AB") == 1, "First test error: " + str(candidate("AB"))      
    assert candidate("1077E") == 2, "Second test error: " + str(candidate("1077E"))  
    assert candidate("ABED1A33") == 4, "Third test error: " + str(candidate("ABED1A33"))      
    assert candidate("2020") == 2, "Fourth test error: " + str(candidate("2020"))  
    assert candidate("123456789ABCDEF0") == 6, "Fifth test error: " + str(candidate("123456789ABCDEF0"))      
    assert candidate("112233445566778899AABBCCDDEEFF00") == 12, "Sixth test error: " + str(candidate("112233445566778899AABBCCDDEEFF00"))  


    # Check some edge cases that are easy to work out by hand.
    assert candidate([]) == 0

def hex_key(num):
    prime_digits = {
        '2': False, '3': False, '5': False, '7': False,
        'B': True, 'D': True, 'F': False,
        other: False for other in '014689ACE'
    }

    for digit in num.upper():
        if prime_digits[digit]:
            prime_digits['total'] += 1

    return prime_digits['total']
candidate = hex_key
check(candidate)