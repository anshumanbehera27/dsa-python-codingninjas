from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)


def reverseStack(inputStack, extraStack):
    if (len(inputStack) < 1):
        return
    # Your code goes here
    while (len(inputStack) != 1):
        ele = inputStack.pop()
        extraStack.append(ele)

    lastele = inputStack.pop()

    while (len(extraStack) != 0):
        ele = extraStack.pop()
        inputStack.append(ele)

    reverseStack(inputStack, extraStack)
    inputStack.append(lastele)

    return inputStack


'''-------------- Utility Functions --------------'''


# Taking input using fast I/o method
def takeInput():
    size = int(input())
    inputStack = list()

    if size == 0:
        return inputStack

    values = [int(x) for x in input().split()]
    inputStack = values

    return inputStack


# main
inputStack = takeInput()
emptyStack = list()

reverseStack(inputStack, emptyStack)

while (len(inputStack) != 0):
    print(inputStack.pop(), end=" ")