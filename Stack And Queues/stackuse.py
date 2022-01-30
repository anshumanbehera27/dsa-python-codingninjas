from stack import Stack


s = Stack()
s.push(12)
s.push(14)
s.push(23)
while s.isempty() is False:
    print(s.pop())

