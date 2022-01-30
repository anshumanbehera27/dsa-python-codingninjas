import heapq



def kSmallest(arr, k):
    heap = arr[:k]
    heapq.heapify(heap)
    n = len(arr)
    for i in range(k, n):
        if heap[0] <arr[i]:
            heapq.heapreplace(heap, arr[i])
    return heap


arr = [2 ,12,9,16,10,5,3,20,25,11,1,8,6]
k = 4
elements = kSmallest(arr, 4)
for ele in elements:
    print(ele, end=" ")
