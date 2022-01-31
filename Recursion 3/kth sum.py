import sys

sys.setrecursionlimit(10 ** 8)


def subsetsSumK(arr, si=0,k ):
    # Your code goes here

    # base case
    if si == len(arr):
        if k == 0:
            return [[]]
        else:
            return [[]]

    # call recursion with  including  the 1st ele
    temp1 = subsetsSumK(arr, si + 1, k - arr[si])
    # call recursion with out including 1st ele
    temp2 = subsetsSumK(arr, si, k)
    output = [[]]
    output.append(arr[0])
    output.append(temp1)
    output.append(temp2)
    return output

