def check(candidate):

    # Check some simple cases
    assert candidate(0) == "db0db"
    assert candidate(32) == "db100000db"
    assert candidate(103) == "db1100111db"
    assert candidate(15) == "db1111db", "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"

def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]
    binary_with_db = "db" + binary + "db"
    return binary_with_db
candidate = decimal_to_binary
check(candidate)