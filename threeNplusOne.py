# 3n + 1 problem

def cycleLen(n):

    count = 1
    while (n > 1):
        if n % 2 == 0:
            n = n // 2
        else:
            n = (3 * n) + 1
        count += 1
    return count


def maxCycleLen(i, j):
    maxLen = 0
    for k in range(i, j + 1):
        maxLen = max(maxLen, cycleLen(k))
    return maxLen
print("solution.......")
print(maxCycleLen(1, 10))
print(maxCycleLen(100, 200))
print(maxCycleLen(900, 100000))

#Optimized using Memo

def cycleLenOpt(n, memo = {}):
    if n == 1:
        return 1
    if n in memo:
        return memo[n]
    if n % 2 == 0:
        length = 1 + cycleLenn(n //2, memo)
    else:
        length = 1 + cycleLenn(3 * n + 1, memo)
    memo[n] == length
    return length

def maxcycleLenOpt(i, j):
    return max(cycleLenOpt(i) for i in range(i, j + 1))
print("opt solution.....")
print(maxCycleLen(1, 10))
print(maxCycleLen(100, 200))
print(maxCycleLen(900, 100000))


    
    
        

    
    