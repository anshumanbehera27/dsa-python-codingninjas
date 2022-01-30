import  heapq
li = [1,5,4,8,7,9,11]
heapq.heapify(li)
#print(li)

heapq.heappush(li,2) # by this we have to add the element in the heap
print(li)
heapq.heappop(li) # by this we have to remove the element from the heap
print(li)
heapq.heapreplace(li , 6 ) # it is used to replace the first elelment in the heap 
print(li)
