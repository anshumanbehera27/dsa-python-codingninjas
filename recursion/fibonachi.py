def fiob(n):
    if n < 2 :
        return n
    return fiob(n-1) + fiob(n-2)
n = int(input())
print(fiob(n))


