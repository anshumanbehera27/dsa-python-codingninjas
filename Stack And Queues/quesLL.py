import  queue
# inbuild stack as List
#s = [1,2,3,4,5]
#s.append(4)
#s.append(5)
#print(s.pop())
#print(s.pop())
# inbuilt ques
#q = queue.Queue() #how ques will work
#q.put(1)
#q.put(2)
##q.put(3)
#q.put(4)
#while not q.empty():
 ##   print(q.get())
q = queue.LifoQueue()
q.put(1)
q.put(3)
q.put(2)
while not q.empty():
    print(q.get())