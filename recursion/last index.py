
def lastindex(arr, x):
    l = len(arr)
    if l == 0:
        return -1
    smalleroutput = arr[1:]
    smallerlistoutput = lastindex(smalleroutput, x)
    if smallerlistoutput != -1:
        return smallerlistoutput + 1
    else:
        if arr[0] == x:
            return 0
        else:
            return -1
arr = [int(x) for x in input().split()]
x = int(input())
print(lastindex(arr,x))