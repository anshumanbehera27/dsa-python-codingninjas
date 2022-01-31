## Read input as specified in the question.
## Print output as specified in the question.
# Problem ID 328 Midpoint LL
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


import sys

sys.setrecursionlimit(100000000)


def recursion(head):
    if (head == None):
        return 1
    temp = recursion(head.next)
    if temp != 1:
        return head
    if head.data < 9:
        head.data += temp
        return head
    else:
        head.data = 0
        return 1


def nextNumber(head):
    # Implement Your Code here
    temp = recursion(head)
    if temp == 1:
        temp2 = head
        head = Node(1)
        head.next = temp2
        return head
    else:
        return head
    pass


def ll(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head


def printll(head):
    while head is not None:
        print(head.data, end=' ')
        head = head.next
    return


# Main
# Read the link list elements including -1
arr = [int(ele) for ele in input().split()]
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
head = nextNumber(l)
printll(head)