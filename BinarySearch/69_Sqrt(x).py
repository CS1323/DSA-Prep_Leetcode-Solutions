def mySqrt(x: int) -> int:

    left = res = 0
    right = x

    # Binary search
    while left <= right:

        mid = ((right - left) // 2) + left

        if mid**2 == x:
            return mid
        
        elif mid**2 < x:
            left = mid + 1
            res = mid
            
        else:
            right = mid - 1

    return res

    # Time:  O(log n)
    # Space: O(1)

x = 4
print(mySqrt(x))