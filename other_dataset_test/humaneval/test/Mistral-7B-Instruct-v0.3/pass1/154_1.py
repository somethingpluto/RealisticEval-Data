def check(candidate):

    # Check some simple cases
    #assert True, "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    #assert True, "This prints if this assert fails 2 (also good for debugging!)"
    assert  candidate("xyzw","xyw") == False , "test #0"
    assert  candidate("yello","ell") == True , "test #1"
    assert  candidate("whattup","ptut") == False , "test #2"
    assert  candidate("efef","fee") == True , "test #3"
    assert  candidate("abab","aabb") == False , "test #4"
    assert  candidate("winemtt","tinem") == True , "test #5"

def rotate(s, n):
    return s[-n:] + s[:-n]

def cycpattern_check(a, b):
    b = b + b  # concatenate the word with itself to check rotations
    for i in range(len(b)):
        if b[i:] in a:
            return True
    return False
candidate = cycpattern_check
check(candidate)