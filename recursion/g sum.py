def gsum(n):
    if n == 0 :
        return 1
    small = gsum(n-1)
    return small + 1/(2**n)
n = 4
print(gsum(n))