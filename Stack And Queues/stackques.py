#s = [1 , 2 , 3, 34, 4 ]
#s.append(5)
#s.append(9)
#print(s.pop())
#print(s.pop())
import queue
#q= queue.Queue()
#q.put(1)
#q.put(2)
#q.put(3)
#q.put(4)
#while not q.empty():
  #  print(q.get())
q = queue.LifoQueue()
q.put(1)
q.put(2)
q.put(3)
while not q.empty():
    print(q.get())

from sys import stdin


def isBalanced(expression):
    # Your code goes here
    s = []
    for char in expression:
        if char in "(":
            s.append(expression)
        elif char in ")":
            if (not s or s[-1] != '('):
                return False
            s.pop()
        if (not s):
            return True
        return False


# main
expression = stdin.readline().strip()
if isBalanced(expression):
    print("true")
else:
    print("false")
