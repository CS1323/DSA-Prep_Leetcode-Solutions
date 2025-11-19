def subarraySum(nums, k) -> int:

    count = curr_sum = 0    # count=num of subarrays summing to k; curr_sum=running prefix sum
    prefix_sums = {0:1}     # prefix_sum -> number of times it has occurred
                            # initialized with 0:1 to handle subarrays starting at index 0

    for num in nums:

        curr_sum += num
        diff = curr_sum - k     # calc needed prefix_sum

        count += prefix_sums.get(diff, 0)

        # record the current prefix_sum
        prefix_sums[curr_sum] = 1 + prefix_sums.get(curr_sum, 0)

    return count

    # Time:  O(n)
    # Space: O(n)

nums = [1,1,1]
k = 2
print(subarraySum(nums, k))