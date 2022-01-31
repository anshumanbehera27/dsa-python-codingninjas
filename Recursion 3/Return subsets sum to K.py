import sys

sys.setrecursionlimit(10 ** 8)


def returnsubsetsumk(arr, si, sum):
    if si == len(arr):
        if sum == 0:
            return [list()]

        else:
            return list()
    so1 = returnsubsetsumk(arr, si + 1, sum)
    so2 = returnsubsetsumk(arr, si + 1, sum - arr[si])
    output = (len(so1) + len(so2)) * [0]
    index = 0
    for i in range(len(so1)):
        output[index] = so1[i]
        index += 1
    for i in range(len(so2)):
        output[index] = (len(so2[i]) + 1) * [0]
        output[index][0] = arr[si]
        for j in range(len(so2[i])):
            output[index][j + 1] = so2[i][j]
        index += 1
    return output


# taking input
def takeInput():
    n = int(input().strip())

    if n == 0:
        return list(), 0

    arr = [int(element) for element in list(input().strip().split(" "))]
    return arr, n


# printing the list of lists
def printListOfList(liOfLi):
    for li in liOfLi:
        for elem in li:
            print(elem, end=" ")
        print()


# main
arr, n = takeInput()

if n != 0:
    k = int(input().strip())
    liOfLi = returnsubsetsumk(arr, 0, k)
    printListOfList(liOfLi)

