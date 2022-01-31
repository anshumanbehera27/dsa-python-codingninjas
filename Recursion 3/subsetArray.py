def subArray(arr, si=0, output=[]):
    # base case
    if si == len(arr):
        return output
    # first recursion with out including the 1st element
    temp1 = subArray(arr, si + 1, output)
    newoutput = []
    newoutput.append(temp1)  # fist
    new_ele = str(arr[0]) + str(newoutput)
    temp2 = subArray(arr, si + 1, new_ele)
    newoutput.append(temp2)
    return output


arr = [int(x) for x in input().split()]
ans = subArray(arr, 0, output=[])

