class BinaryTreesnode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


import queue


def takeLevelwiseInput():
    q = queue.Queue()
    print("enter root")
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTreesnode(rootData)
    q.put(root)
    while (not (q.empty())):
        current_node = q.get()
        print("enter the left child of ", current_node.data)
        leftChildData = int(input())
        if leftChildData != -1:
            leftChildData = BinaryTreesnode(leftChildData)
            current_node.left = leftChildData
            q.put(leftChildData)
        print("enter the right child of ", current_node.data)
        rightChildData = int(input())
        if rightChildData != -1:
            rightChildData = BinaryTreesnode(rightChildData)
            current_node.right = rightChildData
            q.put(rightChildData)
    return root
def printtreeditels(root):
    if root == None:
        return
    print(root.data, end=":")
    if root.left is not None:
        print("L", root.left.data, end=",")
    if root.right is not None:
        print("r", root.right.data, end=',')
    print()
    printtreeditels(root.left)
    printtreeditels(root.right)


def minTree(root):
    if root == None:
        return 10000
    leftmin = minTree(root.left)
    rightmin = minTree(root.right)
    return min(leftmin, rightmin, root.data)




def maxTree(root):
    if root == None:
        return -10000
    leftmax = maxTree(root.left)
    rightmax = maxTree(root.right)
    return max(leftmax, rightmax, root.data)


def isBST(root):
    if root == None:
        return True
    leftmax = maxTree(root.left)
    rightmin = minTree(root.right)
    if root.data > rightmin or root.data <= leftmax:
        return False
    isLeftBST = isBST(root.left)
    isRightBST = isBST(root.right)
    return isLeftBST and isRightBST


root = takeLevelwiseInput()
printtreeditels(root)
isBST(root)
