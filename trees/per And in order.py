class BinaryTreesnode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def bulidTree(pre,inord):
    if len(pre) == None: # base case of it
        return None
    # creat the node of it
    rootdata = pre[0]
    root = BinaryTreesnode(rootdata)
    rootindex = -1
    for i in range(0,len(inord)):
        if inord[i] == rootdata:
            rootindex = i
            break
        if rootindex == -1 :
            return None
        leftInorder =inord[0:rootindex]
        rightInorder = inord[rootindex+1:]
        lenlefttree = len(leftInorder)
        leftpreorder = pre[1:lenlefttree+1]
        rightpreorder = pre[lenlefttree+1 :]
        leftchild = bulidTree(leftpreorder,leftInorder)
        rightchild = bulidTree(rightpreorder,rightInorder)


        root.left = leftchild
        root.right = rightchild
        return root


def printLevelWise(root):
    if root is None:
        return

    pendingNodes = queue.Queue()
    pendingNodes.put(root)
    pendingNodes.put(None)

    while not pendingNodes.empty():
        frontNode = pendingNodes.get()

        if frontNode is None:
            print()

            if not pendingNodes.empty():
                pendingNodes.put(None)

        else:
            print(frontNode.data, end=" ")

            if frontNode.left is not None:
                pendingNodes.put(frontNode.left)

            if frontNode.right is not None:
                pendingNodes.put(frontNode.right)




pre = [1 , 2 , 4, 5 , 3,6,7]
inord = [4,2,5,1,6,3,7]
root =bulidTree(pre,inord)
printLevelWise(root)

