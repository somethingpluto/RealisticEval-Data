

METADATA = {}


def check(candidate):
    assert candidate(8, 3) == "22"
    assert candidate(9, 3) == "100"
    assert candidate(234, 2) == "11101010"
    assert candidate(16, 2) == "10000"
    assert candidate(8, 2) == "1000"
    assert candidate(7, 2) == "111"
    for x in range(2, 8):
        assert candidate(x, x + 1) == str(x)

def change_base(x, base):
    if x == 0:
        return ''
    else:
        digit = str(x % base)
        return change_base(x // base, base) + digit

def main():
    for x in [8, 7, 10, 15]:
        for base in [2, 3, 16]:
            result = change_base(x, base)
            print(f"{x} base {base} = {result}")

if __name__ == "__main__":
    main()
candidate = change_base
check(candidate)