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
    # Split the sentence into a list of words
    words = sentence.split()
    
    # Initialize an empty list to store the prime numbers
    prime_numbers = []
    
    # Iterate over the words in the sentence
    for word in words:
        # Check if the word is a prime number
        if is_prime(word):
            # Add the prime number to the list of prime numbers
            prime_numbers.append(word)
            
            # Remove the word from the sentence
            sentence = sentence[:word.length] + sentence[word.length:]
        else:
            # If the word is not a prime number, remove it from the sentence
            sentence = sentence[:word.length] + sentence[word.length:]
    
    # Return the list of prime numbers
    return prime_numbers

candidate = words_in_sentence
check(candidate)