def check(candidate):

    # Check some simple cases
    assert candidate([3, 4, 5, 1, 2])==True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([3, 5, 10, 1, 2])==True
    assert candidate([4, 3, 1, 2])==False
    # Check some edge cases that are easy to work out by hand.
    assert candidate([3, 5, 4, 1, 2])==False, "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate([])==True

def move_one_ball(arr):
    n = len(arr)
    if n == 1:
        return True
    dp = [[0] * n for _ in range(n + 1)]
    dp[1][0] = 1
    for i in range(2, n + 1):
        dp[i][0] = dp[i - 1][0] + dp[i - 1][i]
    for i in range(1, n + 1):
        for j in range(i - 1, 0, -1):
            dp[i][j] = dp[i - 1][j]
    return dp[n][n]

candidate = move_one_ball
check(candidate)