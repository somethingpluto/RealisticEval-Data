def check(candidate):

    # Check some simple cases
    assert candidate("apple") == False
    assert candidate("apple pi e") == True
    assert candidate("eeeee") == False
    assert candidate("A") == True
    assert candidate("Pumpkin pie ") == False
    assert candidate("Pumpkin pie 1") == False
    assert candidate("") == False
    assert candidate("eeeee e ") == False
    assert candidate("apple pie") == False
    assert candidate("apple pi e ") == False

    # Check some edge cases that are easy to work out by hand.
    assert True

 
check_if_last_char_is_a_letter("apple pie")
 
check_if_last_char_is_a_letter("apple pi e")
 
check_if_last_char_is_a_letter("apple pi e ")
 
check_if_last_char_is_a_letter("")

candidate = check_if_last_char_is_a_letter
check(candidate)