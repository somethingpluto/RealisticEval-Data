

METADATA = {}


def check(candidate):
    from random import randint, choice
    import copy
    import string

    letters = string.ascii_lowercase
    for _ in range(100):
        str = ''.join(choice(letters) for i in range(randint(10, 20)))
        encoded_str = encode_shift(str)
        assert candidate(copy.deepcopy(encoded_str)) == str


s = "hello world"
decoded_s = decode_shift(s)
print(decoded_s)  # Output: "hello world"

candidate = decode_shift
check(candidate)