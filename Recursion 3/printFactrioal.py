def printFacrioal(n,ans):
    if n == 0 :
        print(ans)
        return
    ans = ans * n
    printFacrioal(n-1,ans)
print(printFacrioal(5,1) )