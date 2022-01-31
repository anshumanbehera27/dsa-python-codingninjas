def printSub(s, o):
    if len(s) == 0:
        print(o)
        return
        # call with out including 0th part
    printSub(s[1:], o)
    # call including j
    newOutput = o + s[0]
    printSub(s[1:], newOutput)


s = input()
printSub(s, "")



