class Quesusingtwostack:
    def __init__(self):
        self.__s1 = []
        self.__s2 = []
    def enque(self,data):
        while(len(self.__s1) != 0):
            self.__s2.append(self.__s1.pop())
        self.__s1.append(data)
        while (len(self.__s2) != 0):
            self.__s1.append(self.__s2.pop())
        return



    def deque(self):
        if(len(self.__s1)== 0):
            return -1
        return self.__s1.pop()
    def front(self):
        if(len(self.__s1) == 0 ):
            return -1
        return  self.__s1[-1]
    def size(self):
        return len(self.__s1)
    def isempy(self):
        return self.size() == 0
q = Quesusingtwostack()
q.enque(1)
q.enque(2)
q.enque(3)
q.enque(4)
q.enque(5)
while (q.isempy() is False):
    print(q.front())
    q.deque()
