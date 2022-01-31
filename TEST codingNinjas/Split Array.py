
def split(arr ,i ,s1 ,s2=0):
    # Implement Your Function here
    if i== len(arr):
        if s1 == s2:
            return True
        else:
            return False

    if arr[i] % 5 == 0:
        s1 += arr[i]
        return split(arr, i + 1, s1, s2)
    elif arr[i] % 3 == 0:
        s2 += arr[i]
        return split(arr, i + 1, s1, s2)
    else:
        a = split(arr, i + 1, s1 + arr[i], s2)
        b = split(arr, i + 1, s1, s2 + arr[i])
        return a or b


n = input()
arr = [int(ele) for ele in input().split()]
ans = split(arr, 0, 0)
if ans is True:
    print('true')
else:
    print('false')
