from sys import stdin


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def evenAfterOdd(head):
    # Your code goes here
    if head == None:
        return head
    eh = None
    et = None
    oh = None
    ot = None
    while head != None:
        if head.data % 2 == 0:
            if eh == None:
                eh = head
                et = head
            else:
                et.next = head
                et = head
            head = head.next
        else:
            if oh == None:
                oh = head
                ot = head
            else:
                ot.next = head
                ot = head
            head = head.next
    if oh == None:
        return eh
    if eh == None:
        return oh
    ot.next = None
    et.next = None
    ot.next = eh
    return oh


# Taking Input Using Fast I/O
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


# to print the linked list
def printLinkedList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


# main
t = int(stdin.readline().rstrip())

while t > 0:
    head = takeInput()
    newHead = evenAfterOdd(head)
    printLinkedList(newHead)

    t -= 1