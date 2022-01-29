from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# def findNodeRec(head, n) :
# 	#Your code goes here
#     if head == None or head.next == None:
#         return head
#     count = 0
#     s = head.next
#     if s.data == n:
#         return count
#     small = findNodeRec(head.next,n)
#     count = count +1
#     if head.data == n :
#         return count
#     else:
#         return -1

def findNodeRec(head, n):
    if head == None:
        return -1

    if head.data == n:
        return 0

    count = findNodeRec(head.next, n)
    if count != -1:
        return 1 + count
    else:
        return -1


def takeInput():
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1):
        data = datas[i]
        newNode = Node(data)

        if head is None:
            head = newNode
            tail = newNode

        else:
            tail.next = newNode
            tail = newNode

        i += 1

    return head


def printLinkedList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


# main
t = int(stdin.readline().rstrip())

while t > 0:
    head = takeInput()
    n = int(stdin.readline().rstrip())

    print(findNodeRec(head, n))

    t -= 1