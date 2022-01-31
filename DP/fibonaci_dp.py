def fibo(n , dp):
   if n == 0 or n == 1 : # base case
       return n
   if dp[n-1] == -1 :
       ans1 = fibo(n-1,dp)
       dp[n-1] = ans1
   else:
       ans1 = dp[n-1]
   if dp[n-2] == -1 :
       ans2 = fibo(n-2 , dp)
       dp[n-2] = ans2
   else:
       ans2 = dp[n-2]


   myans = ans1 + ans2
   return myans
n = int(input())
dp = [-1 for i in range(n+1)]
ans = fibo(n, dp)
print(ans)
