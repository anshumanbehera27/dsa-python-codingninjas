import math
import sys


def min_squre(n):
    if n == 0 : # base case
        return 0
    ans = sys.maxsize
    root = int(math.sqrt(n))
    for i in range(1,root+1):
        currAns = 1 + min_squre(n-(i**2))
        ans = min(ans,currAns)

    return ans
n = int(input())
ans = min_squre(n)
print(ans)