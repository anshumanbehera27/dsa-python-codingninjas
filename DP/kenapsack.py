def knapsack(w,val,wt,n,i):
    if i == n :
        return 0

    if wt[i] > w :
        ans = knapsack(w,val,wt,n,i+1)

    else:
        ans1 = val[i] + knapsack(w-wt[i],val,wt,n,i+1)

        ans2 = knapsack(w,val,wt,n,i+1)
        ans = max(ans1,ans2)
    return ans






val = [200,300,100]
wt = [20,25,30]
w = 50
n = len(val)
ans = knapsack(w,val,wt,n,0)
print(ans)