class Stack:
    def __init__(self):
        self.__data = []
    def push(self,ele):
        self.__data.append(ele)
    def pop(self):
        if self.isempty is True:
            print(" hey it is empty ")
            return
        return self.__data.pop()
    def top(self):
        if self.isempty is True:
            print(" hey this is empty ")
            return
        return self.__data[len(self.__data)-1]
    def size(self):
        return len(self.__data)
    def isempty(self):
        return self.size() == 0




