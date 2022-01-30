from sys import stdin
import queue


class Stack:

    # Define data members and _init_()
    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()

    def getSize(self):
        return self.q1.qsize()

    def isEmpty(self):
        return self.getSize() == 0

    def push(self, data):
        self.q1.put(data)

    def pop(self):
        if self.isEmpty():
            return -1

        while self.getSize() > 1:
            self.q2.put(self.q1.get())

        ans = self.q1.get()
        # swapping the queues
        temp = self.q1
        self.q1 = self.q2
        self.q2 = temp
        return ans

    def top(self):
        if self.isEmpty():
            return -1

        while self.getSize() > 1:
            self.q2.put(self.q1.get())

        ans = self.q1.get()
        self.q2.put(ans)

        temp = self.q1
        self.q1 = self.q2
        self.q2 = temp

        return ans


# class Queue:
#     def _init_(self):
#         self.items = []

#     def is_empty(self):
#         return self.items == []

#     def enqueue(self, data):
#         self.items.append(data)

#     def dequeue(self):
#         return self.items.pop(0)


# main
q = int(stdin.readline().strip())

stack = Stack()

while q > 0:

    inputs = stdin.readline().strip().split(" ")
    choice = int(inputs[0])

    if choice == 1:
        data = int(inputs[1])
        stack.push(data)

    elif choice == 2:
        print(stack.pop())

    elif choice == 3:
        print(stack.top())

    elif choice == 4:
        print(stack.getSize())

    else:
        if stack.isEmpty():
            print("true")
        else:
            print("false")

    q -= 1