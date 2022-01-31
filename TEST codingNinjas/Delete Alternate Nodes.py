'''
    Following is the node structure

class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

'''


def deleteAlternateNodes(head):
    if head == None or head.next == None:
        return head

    head.next = deleteAlternateNodes(head.next.next)
    return head