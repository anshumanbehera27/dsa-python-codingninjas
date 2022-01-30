def checkMaxHeap(arr):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    parentIndex = 0
    n = len(arr)
    leftIndex = 2 * parentIndex + 1
    rightIndex = 2 * parentIndex + 2
    while (leftIndex < n):

        if arr[parentIndex] > arr[leftIndex] and arr[parentIndex] > arr[rightIndex]:
            return True
        else:
            return False
        parentIndex = leftIndex
        leftIndex = 2 * parentIndex + 1
        rightIndex = 2 * parentIndex + 2
        leftindex += 1
        #############################
    pass


# Main Code
n = int(input())
arr = list(int(i) for i in input().strip().split(' '))

if checkMaxHeap(arr):
    print("true")
else:
    print('false')