import sys


def mincost(cost,i,j,n,m):
    # special case for stope the calling
    if i == n-1 and j == m-1:
        return cost[i][j]
    # wē have to put the base case
    if i >= n or j >= m: # it will check if the value is not going out side of the matrix
        return sys.maxsize

    ans1 = mincost(cost,i,j+1,n,m) # down
    ans2 = mincost(cost,i+1,j,n,m) # up
    ans3 = mincost(cost,i+1,j+1,n,m) #digonal
    ans = cost[i][j]  + min(ans1,ans2,ans3) # cost[i][j] will retuen the last value of the matrix remaing value are callby it self
    return ans






cost = [[1,5,4] , [8,13, 12] ,[2,3,7],[15,16,18]]
ans = mincost(cost,0,0,4,3)
print(ans)