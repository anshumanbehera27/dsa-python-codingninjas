from sys import stdin


def countBracketReversals(s):
    a = []
    if len(s) % 2 != 0:
        return -1
    for i in s:
        if i == "{":
            a.append(i)
        else:
            if len(a) == 0:
                a.append(i)
            elif a[-1] == "{":
                a.pop()
            else:
                a.append(i)

    count = 0
    while len(a) != 0:
        c1 = a.pop()
        c2 = a.pop()
        if c1 == c2:
            count = count + 1
        else:
            count = count + 2

    return count


# main
print(countBracketReversals(stdin.readline().strip()))