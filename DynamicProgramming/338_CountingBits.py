def countBits(n: int):

    dp = [0] * (n+1)
    offset = 1  # max power of 2 reached so far

    # Bottom-Up DP
    for i in range(1, n+1):

        # update power of 2 offset
        if offset * 2 == i:
            offset = i

        dp[i] = 1 + dp[i - offset]

    return dp

    # Time:  O(n)
    # Space: O(1)   extra space

n = 2
print(countBits(n))