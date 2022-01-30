class priorityQueueNode:
    def __init__(self, ele, priority):
        self.ele = ele
        self.priority = priority


class PriorityQueue:
    def __init__(self):
        self.pq = []

    def isEmpty(self):
        # Implement the isEmpty() function here
        return self.getSize() == 0

    def getSize(self):
        # Implement the getSize() function here
        return len(self.pq)

    def getMax(self):
        # Implement the getMax() function here
        return self.pq[0].ele

    def __perculateUp(self, ele, priority):
        childIndex = self.getSize() - 1
        while childIndex > 0:
            parentIndex = (childIndex - 1) // 2
            if self.pq[childIndex].priority > self.pq[parentIndex].priority:
                self.pq[childIndex], self.pq[parentIndex] = self.pq[parentIndex], self.pq[childIndex]
                chidIndex = parentIndex
            else:
                break

    def insert(self, ele, priority):
        # Implement the insert() function here
        pqNode = priorityQueueNode(ele, priority)
        self.pq.append(pqNode)
        self.__perculateUp()

    def __perculateDown(self, ele, priority):
        parentIndex = 0
        leftIndex = 2 * parentIndex + 1
        rightIndex = 2 * parentIndex + 2
        while leftIndex < self.getSize():
            maxIndex = parentIndex
            if self.pq[maxIndex].priority < self.pq[leftIndex].priority:
                maxIndex = leftIndex
            if self.pq[maxIndex].priority < self.pq[rightIndex].priority:
                maxIndex = rightIndex
            if maxIndex == parentIndex:
                break
            self.pq[maxIndex], self.pq[parentIndex] = self.pq[parentIndex], self.pq[maxIndex]
            parentIndex = maxIndex

            leftIndex = 2 * parentIndex + 1
            rightIndex = 2 * parentIndex + 2

    def removeMax(self):
        # Implement the removeMax() function here
        if self.isEmpty() == 0:
            return True
        ans = self.pq[0].ele
        self.pq[0].ele = self.pq[self.getSize() - 1].ele
        self.pq.pop()
        self.__perculateDown()
        return ans.ele


myPq = PriorityQueue()
curr_input = [int(ele) for ele in input().split()]
choice = curr_input[0]
i = 1
while choice != -1:
    if choice == 1:
        element = curr_input[i]
        i += 1
        pq.insert(element, element)
    elif choice == 2:
        print(pq.getMax())
    elif choice == 3:
        print(pq.removeMax())
    elif choice == 4:
        print(pq.getSize())
    elif choice == 5:
        if pq.isEmpty():
            print('true')
        else:
            print('false')
        break
    else:
        pass
    choice = curr_input[i]
    i += 1