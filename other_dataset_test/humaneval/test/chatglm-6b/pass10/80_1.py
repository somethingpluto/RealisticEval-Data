def check(candidate):

    # Check some simple cases
    assert candidate("a") == False , "a"
    assert candidate("aa") == False , "aa"
    assert candidate("abcd") == True , "abcd"
    assert candidate("aabb") == False , "aabb"
    assert candidate("adb") == True , "adb"
    assert candidate("xyy") == False , "xyy"
    assert candidate("iopaxpoi") == True , "iopaxpoi"
    assert candidate("iopaxioi") == False , "iopaxioi"

print(is_happy("abcd"))  # True
print(is_happy("a"))     # False
print(is_happy("aa"))    # False
print(is_happy("abcd"))  # True
print(is_happy("aabb"))  # False
print(is_happy("adb"))   # True
print(is_happy("xyy"))   # False

candidate = is_happy
check(candidate)