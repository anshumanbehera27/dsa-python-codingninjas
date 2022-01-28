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
root = takeLevelwiseInput()
printtreeditels(root)
def findPathBST(root, k):

    if root is None:
        return None


    if k == root.data:
        output = []
        output.append(root.data)
        return output
    elif k < root.data:
        output = findPathBST(root.left, k)
        if output is not None:
            output.append(root.data)
        return output
    else:
        output = findPathBST(root.right, k)
        if output is not None:
            output.append(root.data)
        return output

k = int(input())
root = takeLevelwiseInput()
printtreeditels(root)
print(findPathBST(root, k ))