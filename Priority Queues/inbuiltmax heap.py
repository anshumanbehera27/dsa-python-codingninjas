import heapq
li = [1,5,4,7,8,9,2,3]
heapq._heapify_max(li) # by this we can  find the max heap

print(li)
# remove a ele from the maximu hepa
heapq._heappop_max(li)
print(li)
heapq._heapreplace_max(li,0)
print(li)

li.append(6)
heapq._siftdown_max(li,0,len(li)-1)
print(li)