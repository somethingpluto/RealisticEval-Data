def check(candidate):

    assert candidate(5) == 1
    assert candidate(6) == 4
    assert candidate(10) == 36
    assert candidate(100) == 53361

def get_max_triples(n):
    count = 0
    for i in range(n):
        a = [i * i - i + 1]
        for j in range(n):
            for k in range(n):
                if a[j] + a[k] + a[i] % 3 == 0:
                    count += 1
    return count

candidate = get_max_triples
check(candidate)