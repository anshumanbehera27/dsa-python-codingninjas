def subs(l):
    if l == []:
        return [[]]

    x = subs(l[1:])

    return x + [[l[0]] + y for y in x]
x = list(input())
n=list(int(i) for i in input().strip().split(' '))
x = subs(n)
for i in x:
    for j in i:
        print(j, end = " ")
    print()