def sort(arr,n):
    if n == 0 or n == 1 :
        return True
    if arr[0] > arr[1]:
        return False
    return sort(arr[1:],n-1)
arr = [int(x)for x in input().split()]
n = int(input())
if sort(arr,n):
    print("yes")
else:
    print("no" )