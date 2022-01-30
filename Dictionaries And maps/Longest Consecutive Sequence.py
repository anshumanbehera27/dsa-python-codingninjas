from sys import stdin


def longestConsecutiveSubsequence(arr, n):
    # Write your code here
    visited = {}
    e_to_i = {}
    for i in range(n):
        e_to_i[arr[i]] = i
        if arr[i] not in visited:
            visited[arr[i]] = True
    lcs = []
    maxi = 1
    min_start = 0
    for i in range(n):
        num = arr[i]
        curr_start = i
        count = 0
        tempNum = num

        while tempNum in visited and visited[tempNum] == True:
            visited[tempNum] = False
            count += 1
            tempNum += 1

        tempNum = num - 1
        while tempNum in visited and visited[tempNum] == True:
            visited[tempNum] = False
            count += 1
            curr_start = e_to_i[tempNum]
            tempNum -= 1

        if count > maxi:
            maxi = count
            min_start = curr_start
        elif maxi == count:
            if min_start > curr_start:
                min_start = curr_start

    startNum = arr[min_start]
    lcs.append(startNum)
    if maxi > 1:
        lcs.append(startNum + maxi - 1)
    return lcs


def takeInput():
    # To take fast I/O
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0
    arr = list(map(int, stdin.readline().strip().split()))
    return arr, n


# Main
arr, n = takeInput()
ans = longestConsecutiveSubsequence(arr, n)
# This ans array contains two numbers, ie, start and end of longest sequence respectively
print(*ans)