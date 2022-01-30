class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = list()


def printTree(root):
    # this is not a base case it  is a edge case
    if root == None:
        return
    print(root.data)
    for child in root.children:
        printTree(child)


def printTreeDetailed(root):
    if root == None:
        return
    print(root.data, ":", end=" ")
    for child in root.children:
        print(child.data, ",", end="")
    print()
    for child in root.children:
        printTreeDetailed(child)


import queue
def takeTreeInputLevelWise():
    q=queue.Queue()
    print("Enter root")
    rootData=int(input())
    if rootData==-1:
        return None
    root=TreeNode(rootData)
    q.put(root)
    while(not(q.empty())):
        current_node=q.get()
        print("Enter num of children for",current_node.data)
        numChildren=int(input())
        for i in range(numChildren):
            print("Enter next child for",current_node.data)
            childData=int(input())
            child=TreeNode(childData)
            current_node.children.append(child)
            q.put(child)
    return root


def printLevelWiseTree(tree):
    q = queue.Queue()

    if tree is None:
        return
    while (not (q.empty())):
        current_node = q.get()
        print(current_node, ":", end=" ,")
        for child in current_node.children:
            q.put(child)
            print(child.data, end=" ")
        print()


def printLevelWiseTree(tree):
    q = queue.Queue()

    if tree is None:
        return
    while (not (q.empty())):
        current_node = q.get()
        print(current_node, ":", end=" ,")
        for child in current_node.children:
            q.put(child)
            print(child.data, end=" ")
        print()
def numNode(root):
    if root == None:
        return 0

    count = 1
    for child in root.children:
        count = count + numNode(child)
    return count


root = takeTreeInputLevelWise()
printLevelWiseTree(root)
