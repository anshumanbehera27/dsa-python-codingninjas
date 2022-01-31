def printmin(l,minsoFar = 1000000):
    if len(l) == 0:
        print(minsoFar)
        return
    newMin = min(minsoFar,l[0])
    printmin(l[1:],newMin)


l = [2,4,6,8,91,0]
print(printmin(l))
