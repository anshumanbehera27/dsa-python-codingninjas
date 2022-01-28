class BinaryTreesnode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

import queue
def takeLevelwiseInput():
    q = queue.Queue()
    print("enter root")
    rootData = int(input())
    if rootData == -1 :
        return None
    root = BinaryTreesnode(rootData)
    q.put(root)
    while (not(q.empty())):
        current_node = q .get()
        print("enter the left child of ",current_node.data)
        leftChildData = int(input())
        if leftChildData != -1 :
            leftChildData = BinaryTreesnode(leftChildData)
            current_node.left = leftChildData
            q.put(leftChildData)
        print("enter the right child of ", current_node.data)
        rightChildData = int(input())
        if rightChildData != -1:
            rightChildData = BinaryTreesnode(rightChildData)
            current_node.right=  rightChildData
            q.put(rightChildData)
    return root


def printLevelWise(root):
    q = queue.Queue()
    if root is None:
        return None
    q.put(root)
    while not q.empty():
        a = q.get()
        print(a.data, end=":")
        LeftChild = a.left
        if LeftChild != None:
            print("L", end=":")
            print(LeftChild.data, end=",")
            q.put(LeftChild)
        else:
            print("L", end=":")
            print(-1, end=',')
        RightChild = a.right
        if RightChild != None:
            print("R", end=':')
            print(RightChild.data)
            q.put(RightChild)
        else:
            print("R", end=":")
            print(-1)
    return root

def isBST3(root,min_range , max_range):
    if root == None  :
        return True
    if root.data < min_range or root.data > max_range:
        return False
    isLeftok = isBST3(root.left, min_range,root.data -1)
    isrightok = isBST3(root.right ,root.data , max_range)
    return isLeftok and isrightok
root = takeLevelwiseInput()
printLevelWise(root)
print(isBST3(root,-100000,1000000))