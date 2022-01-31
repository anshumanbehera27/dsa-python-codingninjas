def tribonachi(n):
    if n < 2 :
        return n
    arr = [0] * 38
    arr[0] = 0
    arr[1] = 1
    arr[2] = 1
    for i in range(3,n+1):
        arr[i] = arr[i-1] + arr[i-2] + arr[i-3]
    return arr[n]
n = int(input())
ans = tribonachi(n)
print(ans)








n = int(input())
ans = tribonachi(n)
print(ans)
