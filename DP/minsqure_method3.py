import math
import sys


def minsqure(n):
    dp=[-1 for i in range(n+1) ]
    dp[0] = 0
    for i in range(1,n+1):
        ans = sys.maxsize
        root = int(math.sqrt(i))
        for j in range(1,root+1):
            cur_ans = 1 + dp[i-(j**2)]
            ans = min(ans , cur_ans)
        dp[i] = ans
    return dp[n]
n  = int(input())
ans = minsqure(n)
print(ans)