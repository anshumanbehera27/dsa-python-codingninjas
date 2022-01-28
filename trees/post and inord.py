def buildTree(post, inord, n):
    # Your code goes here
    if len(post) == None:
        return None
    rootdata = post[len(post) - 1]
    root = BinaryTreeNode(rootdata)
    rootindex = -1
    for i in range(0, len(inord)):
        if inord[i] == rootdata:
            rootindex = i
            break
        if rootindex == -1:
            return None
        leftinorder = inord[0:rootindex]
        rightinorder = inord[rootindex + 1:]
        leftsubtree = len(leftinorder)
        rightsubtree = len(rightinorder)

        leftpostord = post[0:leftsubtree + 1]
        rightpostord = post[leftsubtree + 1:rightsubtree]

        leftchild = buildTree(leftinorder, leftpostorder, n)
        rightchild = buldTree(rightinorder, rightpostorder, n)

        root.left = leftchild
        root.right = rightchild
        return root























