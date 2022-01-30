def uniqueChar(s):
    newstring = " "
    for i in s :
        print(newstring)
        if i not in newstring:
            print(newstring)
            newstring += i
    return newstring
    pass


# Main
s = input()
print(uniqueChar(s))

