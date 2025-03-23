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
    if len(sentence)!= 1:
        raise ValueError("The sentence must be a single word")

    prime_lengths = []
    words = set(sentence)
    for word in sentence.split():
        if len(word) % 2!= 0:
            prime_lengths.append(len(word))
            words.remove(word)
    
    return ''.join([word for word in words if len(word) % 2 == 0])

candidate = words_in_sentence
check(candidate)