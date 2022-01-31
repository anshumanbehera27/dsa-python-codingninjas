def contains(s, t):
    l1 = len(s)
    l2 = len(t)

    i = 0;
    j = 0;

    while i < l1 and j < l2:
        if s[i] == t[j]:
            j += 1
        i += 1

    if j == l2:
        return True
    return False


s = input()
t = input()

ans = contains(s, t)
if ans is True:
    print('true')
else:
    print('false')