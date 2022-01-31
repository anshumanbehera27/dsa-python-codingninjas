# def lis(arr, i, n):
#     if i == n:
    #     return 0, 0
    # including_max = 1
    # for j in range(i + 1):
    #     if arr[j] >= arr[i]:
    #         further_incuding_max = lis(arr, j, n)[0]
    #         including_max = max(including_max, 1 + further_incuding_max)
    #     excluding_max = lis(arr, i + 1, n)[1]
    #     overallmax = max(including_max, excluding_max)
    #     return including_max, overallmax
    #

# n = int(input())
# arr = [int(ele) for ele in input().split()]
# ans = lis(arr, 0, n)[1]
# print(ans)
# def lis(li,i,n):
#     if i==n:
#         return 0,0
#     including_max=1
#     for j in range(i+1,n):
#         if li[j]>=li[i]:
#             further_including_max=lis(li,j,n)[0]
#             including_max=max(including_max,1+further_including_max)
#     excluding_max=lis(li,i+1,n)[1]
#     overallMax=max(including_max,excluding_max)
#     return including_max,overallMax

def lis(li,i,n,dp):
    if i == n  :
        return 0,0
    indclud_max = 1
    for j in range(i+1,n):
        if li[j] <= li[i]:
            if dp[j] == -1 :
                ans = lis(li,j,n,dp)
                dp[j] = ans
                furter_including_max = ans[0]
            else:
                furter_including_max = dp[j][0]

            indclud_max = max(1+furter_including_max,indclud_max)
    if dp[i+1] == -1 :
        ans = lis(li,i+1,n,dp)
        dp[i+1] = ans
        excluding_max = ans[1]
    else:
        excluding_max = dp[i+1]
    overall_max = max(excluding_max , indclud_max)
    return indclud_max,overall_max


















n=int(input())
li=[int(ele) for ele in input().split()]
dp = [-1 for i in range(n+1)]
ans=lis(li,0,n,dp)[1]

print(ans)