from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


# Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printAtK(root, k):
    if k == 0 and root != None:
        print(root.data)
        return
    if root == None:
        return None
    printAtK(root.left, k - 1)
    printAtK(root.right, k - 1)


def nodesAtDistanceK(root, node, k, string="", q=queue.Queue()):
    if root != None and root.data == node:
        printAtK(root, k)
        for ele in string.split():
            q.put(ele)
        return q, k - 1
    if root == None:
        return None, k

    tempString = str(root.data) + "L " + string
    tempString, k = nodesAtDistanceK(root.left, node, k, tempString)

    if tempString != None:
        details = tempString.get()
        if k == 0:
            printAtK(root, k)
        else:
            if (details[-1] == 'L'):
                printAtK(root.right, k - 1)
            else:
                printAtK(root.left, k - 1)

        return tempString, k - 1

    tempString = str(root.data) + "R " + string
    tempString, k = nodesAtDistanceK(root.right, node, k, tempString)

    if tempString != None:
        details = tempString.get()
        if k == 0:
            printAtK(root, k)
        else:
            if (details[-1] == 'L'):
                printAtK(root.right, k - 1)
            else:
                printAtK(root.left, k - 1)

        return tempString, k - 1
    return tempString, k


# Taking level-order input using fast I/O method
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0

    length = len(levelOrder)

    if length == 1:
        return None

    root = BinaryTreeNode(levelOrder[start])
    start += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        currentNode = q.get()

        leftChild = levelOrder[start]
        start += 1

        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)

        rightChild = levelOrder[start]
        start += 1

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)

    return root


def printLevelWise(root):
    if root is None:
        return

    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)

    while not inputQ.empty():

        while not inputQ.empty():

            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left != None:
                outputQ.put(curr.left)
            if curr.right != None:
                outputQ.put(curr.right)

        print()
        inputQ, outputQ = outputQ, inputQ


# Main
root = takeInput()
target_k = stdin.readline().strip().split(" ")

target = int(target_k[0])
k = int(target_k[1])

nodesAtDistanceK(root, target, k)