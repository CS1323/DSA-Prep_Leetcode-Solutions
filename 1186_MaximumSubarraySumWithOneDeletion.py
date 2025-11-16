def maximumSum(arr) -> int:

    n = len(arr)

    # dp_no_del  = max subarray sum with NO deletion used
    # dp_with_del= max subarray sum WITH one deletion used
    # base cases:
    dp_no_del = arr[0]
    dp_with_del = float("-inf")  # cannot delete the only element and still end at index 0

    max_sum = arr[0]

    for i in range(1, n):

        prev_no_del = dp_no_del

        # start new subarray, or extend previous subarray (Kadane's)
        dp_no_del = max(arr[i], prev_no_del + arr[i])         

        # delete curr element, or extend subarray w/earlier deletion
        dp_with_del = max(prev_no_del, dp_with_del + arr[i]) 

        max_sum = max(max_sum, dp_no_del, dp_with_del)

    # max subarray sum with or without deletion
    return max_sum

    # Time:  O(n)
    # Space: O(1)

arr = [2,-1,-1,10]
print(maximumSum(arr))