def lastStoneWeightII(stones) -> int:

    total_sum = sum(stones)
    target = total_sum // 2     # best possible subset sum to reach

    # dp[t] = True if some subset of stones can sum exactly to t
    dp  = [False] * (target+1)
    dp[0] = True    # base case: sum 0 is always achievable

    # Bottom-Up DP - 0/1 knapsack
    for stone in stones:
        for t in range(target, stone-1, -1):

            if dp[t-stone]:
                dp[t] = True

    # find best achievable t
    for t in range(target, -1, -1):
        if dp[t]:
            return total_sum - 2*t

    # Time:  O(n*target)
    # Space: O(target)

stones = [2,7,4,1,8,1]
print(lastStoneWeightII(stones))