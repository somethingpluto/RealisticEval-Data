def check(candidate):
    assert candidate(4) == False
    assert candidate(6) == False
    assert candidate(8) == True
    assert candidate(10) == True
    assert candidate(11) == False
    assert candidate(12) == True
    assert candidate(13) == False
    assert candidate(16) == True
def is_equal_to_sum_even(n):
    if n % 2!= 0 or n < 4:
        return False

    def helper(target, current_sum, numbers):
        if target == current_sum:
            return True
        if target < current_sum or not numbers:
            return False

        numbers.remove(current_sum)
        for i in range(2, min(target, current_sum) + 1, 2):
            helper(target, current_sum - i, numbers)
            numbers.append(current_sum)

        return False

    numbers = list(range(2, n + 1))
    return helper(n, 0, numbers)
candidate = is_equal_to_sum_even
check(candidate)