def countzero(n):
    if n <0 :
        n = n* -1
    if n< 10 :
        if n == 0 :
            return 1
        return 0
    smallans = countzero(n//10)
    if n % 10 == 0 :
        smallans += 1
    return smallans
n = int(input())
print(countzero(n))