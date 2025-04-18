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

def check_if_last_char_is_a_letter(txt):
    stripped_txt = txt.replace(" ", "")
    if stripped_txt[-1].isalpha() and not stripped_txt[-2:].isalpha():
        return True
    else:
        return False
candidate = check_if_last_char_is_a_letter
check(candidate)