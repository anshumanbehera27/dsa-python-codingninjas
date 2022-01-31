def printPermutations(string, output):
    # Implement Your Code Here


    # base case
    if len(string) == 0:
        print(output)
        return
    for i in range(len(string)):
        c = string[i]
        l = string[0:i]
        r = string[i + 1:]
        rest = l + r

    printPermutations(rest, output + c)

    pass


string = [str(x) for x in input().split()]
output = ""
printPermutations(string, output)

