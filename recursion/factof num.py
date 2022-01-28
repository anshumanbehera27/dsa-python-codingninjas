def fun ( n ):
    if n == 0 :
        return  0
    if n == 1 :
        return n
    return  n * fun(n-1)

n = int(input())
print(fun(n))


