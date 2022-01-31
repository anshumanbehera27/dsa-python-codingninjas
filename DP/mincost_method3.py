import sys
def mincostIratively(cost,n,m):
    dp = [[sys.maxsize for i in range(m + 1)] for j in range(n + 1)]
    for i in range(n-1,-1,-1):
        for j in range(m-1,-1,-1):
            if i == n-1 and j == m-1:
                dp[i][j] = cost[i][j]
            else:
                ans1 = dp[i][j+1]
                ans2 = dp[i+1][j]
                ans3 = dp[i+1][j+1]
                dp[i][j] = cost[i][j] + min(ans1,ans2,ans3)
    return dp[0][0]




cost = [[1,5,4] , [8,13, 12] ,[2,3,7],[15,16,18]]
n =4
m= 3
dp = [ [sys.maxsize for i in range(m +1)] for j in range(n+1)]
ans = mincostIratively(cost,n,m)
print(ans)