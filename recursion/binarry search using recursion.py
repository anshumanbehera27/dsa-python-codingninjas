def binarryserch(arr,hig,low,x):
    if hig >= low :
        mid = (hig + low) // 2
        if arr[mid] == x :
            return mid
        elif arr[mid] > x:
            return binarryserch(arr , low  , mid -1  ,x)
        else:
            return binarryserch(arr,mid+1,hig,x)
    else:
        return  -1
arr =  [ int(x) for x in input().split()]
hig = int(input())
low = int(input())
x= int(input())
print(binarryserch(arr,hig,low,x))
