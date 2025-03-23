def check(candidate):

    # Check some simple cases
    assert candidate("5 apples and 6 oranges",19) == 8
    assert candidate("5 apples and 6 oranges",21) == 10
    assert candidate("0 apples and 1 oranges",3) == 2
    assert candidate("1 apples and 0 oranges",3) == 2
    assert candidate("2 apples and 3 oranges",100) == 95
    assert candidate("2 apples and 3 oranges",5) == 0
    assert candidate("1 apples and 100 oranges",120) == 19
def fruit_distribution(s, n):
    parts = s.split(' and ')
    total_fruits = n
    total_apples = sum(map(lambda x: int(x.split(' ')[0]), parts))
    total_oranges = sum(map(lambda x: int(x.split(' ')[1]), parts))
    total_mangoes = total_fruits - total_apples - total_oranges
    return total_mangoes
candidate = fruit_distribution
check(candidate)