class Stack:
    def __init__(self):
        self.__head = None
        self.__count = 0
    def push (self,ele):
        newNode = Node(ele)
        self.newNode.next = self.__head
        self.__head = newNode
        self.__count+=1
        return
    def pop(self):
        if self.__head == None:
            return -1
        data = self.__head.data
        self.__head = self.__head.next
        self.__count -=1
        return data
    def top(self):
        if self.__head == None:
            return -1
        return self.__head.data
    def getsize(self):
        return self.__count
    def isempty(self):
        return self.getsize() == 0