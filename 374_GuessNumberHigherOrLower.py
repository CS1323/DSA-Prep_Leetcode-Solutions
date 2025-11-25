# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:

    pick = 6

    if num < pick:
        return 1
    elif num > pick:
        return -1
    else: 
        return 0

# binary search
def guessNumber(n: int) -> int:

    left = 1
    right = n

    while left <= right:

        mid = left + ((right - left) // 2)

        if guess(mid) == 1:
            left = mid + 1
        elif guess(mid) == -1:
            right = mid - 1
        else:
            return mid

    # Time:  O(log n)
    # Space: O(1)

n = 10
print(guessNumber(n))