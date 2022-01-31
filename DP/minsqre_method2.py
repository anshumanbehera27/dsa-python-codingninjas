import math
import sys


def min_squre(n,dp):
    if n == 0 : # base case
        return 0
    ans = sys.maxsize
    root = int(math.sqrt(n))
    for i in range(1,root+1):
        newValue = n -(i**2)
        if dp[newValue] == -1:
            smallAns = min_squre(newValue,dp)
            dp[newValue] = smallAns
            currAns = 1 + smallAns

        else:
            currAns = 1 + dp[newValue]
        ans = min(ans,currAns)

    return ans
n = int(input())
dp = [-1 for i in range(n+1)]
ans = min_squre(n,dp)

print(ans)