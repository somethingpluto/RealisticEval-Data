def check(candidate):

    assert candidate(5) == [1, 2, 6, 24, 15]
    assert candidate(7) == [1, 2, 6, 24, 15, 720, 28]
    assert candidate(1) == [1]
    assert candidate(3) == [1, 2, 6]
def f(n):
    result = [None] * n
    for i in range(n):
        if i % 2 == 0:
            result[i] = 1
            for j in range(1, i + 1):
                result[i] *= j
        else:
            result[i] = sum(range(1, i + 1))
    return result
candidate = f
check(candidate)