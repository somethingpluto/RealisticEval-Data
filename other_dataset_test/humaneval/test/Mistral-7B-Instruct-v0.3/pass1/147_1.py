def check(candidate):

    assert candidate(5) == 1
    assert candidate(6) == 4
    assert candidate(10) == 36
    assert candidate(100) == 53361
def get_max_triples(n):
    a = [i * i - i + 1 for i in range(1, n + 1)]
    count = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            for k in range(j + 1, len(a)):
                if a[i] + a[j] + a[k] % 3 == 0:
                    count += 1
    return count
candidate = get_max_triples
check(candidate)