def down_heapify(arr,i,n):
    parentIndex = i
    leftchildIndex = 2 * parentIndex +1
    rightchildIndex  = 2 * parentIndex + 2
    while leftchildIndex < n :
        minIndex = parentIndex
        if arr[minIndex] > arr[leftchildIndex]:
            minIndex = leftchildIndex
        if rightchildIndex < n and arr[minIndex] > arr[rightchildIndex]:
            minIndex = rightchildIndex
        if minIndex == parentIndex:
            return
        arr[minIndex],arr[parentIndex] = arr[parentIndex],arr[minIndex]
        parentIndex = minIndex
        leftchildIndex = 2 * parentIndex +1
        rightchildIndex = 2 * parentIndex + 2
    return






def heapSort(arr):
    n = len(arr)
    # build the arr first
    for i in range(n//2  ,-1,-1):
        down_heapify(arr, i, n)
    for i in range(n-1 ,0 , -1 ):
        arr[0] ,arr[i] = arr[i] , arr[0]
        down_heapify(arr,0,i)
        # remove n ele from the heap and put them at correct position
    return

arr = [int(ele) for ele in input().split()]
heapSort(arr)
for ele in arr:
    print(ele , end= ' ')