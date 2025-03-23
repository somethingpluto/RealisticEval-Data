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
    result = []
    for word in lst:
        if len(word) % 2 == 1:
            result.append(word)
        else:
            result.append(sorted(word))
    return result
scss
assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

candidate = sorted_list_sum
check(candidate)