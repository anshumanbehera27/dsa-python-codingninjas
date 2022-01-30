class prorityQueueNode:
    def __init__(self, value ,priority):
        self.value = value
        self.priority = priority


class priorityQueue:
    def __init__(self):
        self.pq = [ ]
    def getSize(self):
        return len(self.pq)
    def isEmpty(self):
        return self.getSize() == 0
    def getmin(self):
        if self.isEmpty() == 0 :
            return  None

        return self.pq[0].value

    def __percolateUp(self):
        childIndex = self.getSize()-1
        while childIndex > 0 :
            perentIndex = (childIndex-1) //2
            if self.pq[childIndex].priority <self.pq[perentIndex].priority:
                self.pq[childIndex],self.pq[perentIndex] = self.pq[perentIndex] , self.pq[childIndex]
                childIndex = perentIndex
            else:
                break
    def insert(self,value,priority):
        pqNode = prorityQueueNode(value ,priority)
        self.pq.append(pqNode)
        self.__percolateUp()



    def __percolateDown(self): # by the method we have to comper all the ele in the Bst

        parentIndex = 0 #  check the first ele
        leftIndex = 2 * parentIndex + 1  # left elel
        rightIndex = 2 *parentIndex+ 2  # right ele

        while leftIndex < self.getSize(): # run the loop un till it recahed its right position
            minIndex = parentIndex  # we have to  take the min index and swife the ele accordingly
            if self.pq[minIndex].priority > self.pq[leftIndex].priority:
                minIndex = leftIndex
            if rightIndex <self.getSize()  and self.pq[minIndex].priority > self.pq[rightIndex].priority:
                maxIndex = rightIndex

            if minIndex == parentIndex: # if it is eqal then it is going to be end
                break
            self.pq[parentIndex] ,self.pq[minIndex] = self.pq[minIndex] ,self.pq[parentIndex]
            parentIndex = minIndex

            leftIndex = 2 *parentIndex + 1
            rightIndex = 2 * parentIndex + 2
    def Removemin(self):
        if self.isEmpty():
            return None
        ele = self.pq[0].value
        self.pq[0] = self.pq[self.getSize()-1]
        self.pq.pop()
        self.__percolateDown()
        return ele

pq = priorityQueue()
pq.insert('A',10)
pq.insert('c',5)
pq.insert('b',19)
pq.insert('d',4)
for i in range(4):
    print(pq.Removemin())