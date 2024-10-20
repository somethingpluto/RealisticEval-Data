N = int(input())

# generated by gpt-4

def find_powers(num):
    if num == 0:
        return None

    n, m = 0, 0
    while num % 2 == 0:
        n += 1
        num //= 2
    while num % 3 == 0:
        m += 1
        num //= 3

    if num == 1:
        return n, m
    else:
        return None

result = find_powers(N)
if result:
    print('Yes')
else:
    print('No')