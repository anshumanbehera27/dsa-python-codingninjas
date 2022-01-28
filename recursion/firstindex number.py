def firstindex(arr,x):
    if len(arr) == 0 :
        return -1
    if arr[0] == x :
        return  0
    small = firstindex(arr[1:],x)
    if small == -1 :
        return -1
    else:
        return 1 +small
arr= [int(x) for x in input().split()]
x = int(input())
print(firstindex(arr,x))
