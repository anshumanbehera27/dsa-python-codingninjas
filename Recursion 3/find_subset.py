def subsetArray(arr):
    if len(arr) == 0:
        output = []
        output.append("")
        return output
    smallpart = arr[1:]
    smallerOutput = subsetArray(smallpart)

    output = []
    for sub in smallerOutput:
        output.append(str(sub))
    for sub in smallerOutput:
        add_first_ele = str(arr[0]) + str(sub)
        output.append(add_first_ele)


    return output


arr = [int(i) for i in input().split()]
ans = subsetArray(arr)
for i in ans:
    for j in i:
        print(j, end = " ")
    print()





