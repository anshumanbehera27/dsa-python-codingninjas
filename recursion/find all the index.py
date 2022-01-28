def allind(arr,x):
    i = 0
    if len(arr) == 0 :
        return 0
    if arr[0] == x :
        return i
    small = allind(arr[1:],x)
    return 1 + small
arr = [int( x) for x in input().split()]
x = int( input())
print(allind(arr,x))