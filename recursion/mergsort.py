def mergsort(arr):
    if len(arr) <= 1 :
        return arr
    mid = len(arr) // 2
    s1 = arr[0:mid]
    s2 = arr[mid:]
    mergsort(s1)
    mergsort(s2)
    merg(arr,s1,s2)
def merg(arr,s1,s2):
    i = j = k = 0
    while i < len(s1) and j < len(s2):
        if s1[i] < s2[j]:
            arr[k] = s1[i]
            i = i+1
            k=k+1
        else:
            arr[k] = s2[j]
            j=j+1
            k= k+1
    while i < len(s1 ):
        arr[k] = s1 [i]
        i= i+1
        k = k +1
    while j < len(s2):
        arr[k] = s2 [j]
        j= j +1
        k = k + 1

arr = [2,3,4,7,8,9,3,2]
mergsort(arr)
print(*arr)