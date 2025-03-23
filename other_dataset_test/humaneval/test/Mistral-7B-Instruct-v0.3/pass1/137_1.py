def check(candidate):

    # Check some simple cases
    assert candidate(1, 2) == 2
    assert candidate(1, 2.5) == 2.5
    assert candidate(2, 3) == 3
    assert candidate(5, 6) == 6
    assert candidate(1, "2,3") == "2,3"
    assert candidate("5,1", "6") == "6"
    assert candidate("1", "2") == "2"
    assert candidate("1", 1) == None

    # Check some edge cases that are easy to work out by hand.
    assert True

def compare_one(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if a > b:
            return a
        elif a < b:
            return b
        else:
            return None

    if isinstance(a, str) and a.replace(".", "").replace(",", ".").isnumeric() and isinstance(b, (int, float)):
        a_float = float(a.replace(",", "."))
        if a_float > b:
            return a_float
        else:
            return b

    if isinstance(a, (int, float)) and isinstance(b, str) and b.replace(".", "").replace(",", ".").isnumeric():
        b_float = float(b.replace(",", "."))
        if a > b_float:
            return a
        else:
            return b_float

    if isinstance(a, str) and isinstance(b, str) and a.replace(".", "").replace(",", ".").isnumeric() and b.replace(".", "").replace(",", ".").isnumeric():
        a_float = float(a.replace(",", "."))
        b_float = float(b.replace(",", "."))
        if a_float > b_float:
            return a_float
        elif a_float < b_float:
            return b_float
        else:
            return None
candidate = compare_one
check(candidate)