def quicksort(arr,si,ei):
    if si >= ei :
        return
    pi = partition(arr,si,ei)
    quicksort(arr,si,pi-1)
    quicksort(arr,pi+1,ei)
def partition(arr,si,ei):
    s = arr[si]
    c = 0
    for i in range(si,ei+1):
        if arr[i ] < s :
            c=c+1
    arr[si+c] ,arr[si] = arr[si],arr[si+c]
    pi = si+c
    i= 0
    j = ei
    while i<j:
        if arr[i] < s:
            i = i + 1
        elif arr[j] >= s:
            j = j-1
        else:
            arr[i] ,arr[j] = arr[j] ,arr[i]
            i = i+1
            j = j -1
    return pi
arr = [2,7,8,3,5,4,3,2,1]
si = 0
ei = len(arr) -1
quicksort(arr, si, ei)
print(*arr)

