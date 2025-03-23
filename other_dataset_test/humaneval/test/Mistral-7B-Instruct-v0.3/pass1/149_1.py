def check(candidate):

    # Check some simple cases
    assert candidate(["aa", "a", "aaa"]) == ["aa"]
    assert candidate(["school", "AI", "asdf", "b"]) == ["AI", "asdf", "school"]
    assert candidate(["d", "b", "c", "a"]) == []
    assert candidate(["d", "dcba", "abcd", "a"]) == ["abcd", "dcba"]

    # Check some edge cases that are easy to work out by hand.
    assert candidate(["AI", "ai", "au"]) == ["AI", "ai", "au"]
    assert candidate(["a", "b", "b", "c", "c", "a"]) == []
    assert candidate(['aaaa', 'bbbb', 'dd', 'cc']) == ["cc", "dd", "aaaa", "bbbb"]

def sorted_list_sum(lst):
    # Filter out strings with odd lengths
    odd_length_free = [word for word in lst if len(word) % 2 == 0]

    # Sort the list by length and then alphabetically if lengths are equal
    sorted_list = sorted(odd_length_free, key=len)
    for i in range(len(sorted_list)):
        for j in range(i+1, len(sorted_list)):
            if len(sorted_list[i]) == len(sorted_list[j]) and sorted_list[i] > sorted_list[j]:
                sorted_list[i], sorted_list[j] = sorted_list[j], sorted_list[i]

    return sorted_list
candidate = sorted_list_sum
check(candidate)