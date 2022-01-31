import sys


# def minstep(n):
    # if n == 1:
    #     return 0
    # x = sys.maxsize
    # if n % 3 == 0 :
    #     x = minstep(n//3)
    # y = sys.maxsize
    # if n %2 == 0 :
    #     y = minstep(n//2)
    # z = minstep(n-1)
    # ans = 1 + min(x ,y ,z)
    # return ans

# def minstep(n,dp):
    # if n == 1:
    #     return n
    # x = sys.maxsize
    #
    # if n % 3 == 0 :
    #     if dp[n//3] == -1:
    #         x = minstep(n//3,dp)
    #         dp[n//3] = x
    #     else:
    #         x = dp[n//3]
    # y = sys.maxsize
    # if n % 2 == 0 :
    #     if [n//2] == -1:
    #         y = minstep(n//2,dp)
    #         dp[n//2] = y
    #     else:
    #         y = dp[n//2]
    # if dp[n-1] == -1 :
    #     z = minstep(n-1,dp)
    #     dp[n-1] = z
    # else:
    #     z = dp[n-1]
    #
    #
    # return min(x,min(y,z)) + 1


import sys


def minStepsTo1(n, dp):
    if n == 1:
        return 0
    ans1 = sys.maxsize
    if n % 3 == 0:
        if dp[n // 3] == -1:
            ans1 = minStepsTo1(n // 3, dp)
            dp[n // 3] = ans1
        else:
            ans1 = dp[n // 3]
    ans2 = sys.maxsize

    if n % 2 == 0:
        if dp[n // 2] == -1:
            ans2 = minStepsTo1(n // 2, dp)
            dp[n // 2] = ans2
        else:
            ans2 = dp[n // 2]
    if dp[n - 1] == -1:
        ans3 = minStepsTo1(n - 1, dp)
        dp[n - 1] = ans3
    else:
        ans3 = dp[n - 1]

    ans = 1 + min(ans1, ans2, ans3)
    return ans


n = int(input())
dp = [-1 for i in range(n + 1)]
ans = minStepsTo1(n, dp)
print(ans)
