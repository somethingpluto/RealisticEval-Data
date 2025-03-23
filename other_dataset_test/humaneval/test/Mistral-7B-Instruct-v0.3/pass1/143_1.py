def check(candidate):

    # Check some simple cases
    assert candidate("This is a test") == "is"
    assert candidate("lets go for swimming") == "go for"
    assert candidate("there is no place available here") == "there is no place"
    assert candidate("Hi I am Hussein") == "Hi am Hussein"
    assert candidate("go for it") == "go for it"

    # Check some edge cases that are easy to work out by hand.
    assert candidate("here") == ""
    assert candidate("here is") == "is"

def words_in_sentence(sentence):
    words = sentence.split()
    prime_words = []
    for word in words:
        if is_prime(len(word)):
            prime_words.append(word)
    return " ".join(prime_words)

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
candidate = words_in_sentence
check(candidate)