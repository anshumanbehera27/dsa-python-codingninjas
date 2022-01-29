def findNode(head, n) :
    #Your code goes here
    index=0
    while head is not None:
        if(head.data == n):
            return index
        index+=1
        head = head.next
    else:
        return -1






















