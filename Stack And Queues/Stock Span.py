from sys import stdin


def stockSpan(s):
    n = len(s)
    st = []
    st.append(0)
    S = [0 for i in range(len(s) + 1)]
    S[0] = 1

    for i in range(1, n):

        while (len(st) > 0 and s[st[-1]] < s[i]):
            st.pop()

        if len(st) <= 0:
            S[i] = i + 1
        else:
            S[i] = (i - st[-1])

        st.append(i)

    S.pop()
    return S


'''-------------- Utility Functions --------------'''


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")

    print()


def takeInput():
    size = int(stdin.readline().strip())

    if size == 0:
        return list(), 0

    price = list(map(int, stdin.readline().strip().split(" ")))

    return price, size


# main
price, n = takeInput()

output = stockSpan(price)
printList(output)