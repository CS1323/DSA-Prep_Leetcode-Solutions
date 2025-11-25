def isHappy(n: int) -> bool:

    # 19 -> 1**2 + 9**2 = 
    prev = 0

    while n != prev:

        prev = n
        summ = 0

        while n > 0:
            summ += (n % 10)**2
            n //= 10

        n = summ
        print(n, prev) 

    return True if n == 1 else False
    
    # Time:  O()
    # Space: O()

n = 2
print(isHappy(n))