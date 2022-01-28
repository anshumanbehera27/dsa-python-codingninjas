class BinaryTreesnode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def printtreeditels(root):
    if root == None:
        return
    print(root.data, end = ":")
    if root.left != None:
        print("l",root.left.data, end=  ",")
    if root.right != None:
        print("r" ,root.right.data, end= '' )
    print()
    printtreeditels(root.left)
    printtreeditels(root.right)
def takeInput():
    rootData = int(input())
    if rootData == -1 :
        return None
    root = BinaryTreesnode(rootData)
    leftTree = takeInput()
    rightTree = takeInput()
    root.left = leftTree
    root.right = rightTree
    return  root
def reamoveleaf(root):
    if root == None:
        return None
    if root.left == None and root.right == None:
        return None
    root.left =reamoveleaf(root.left)
    root.right = reamoveleaf(root.right)
    return root




root = takeInput()
printtreeditels(root)
root = reamoveleaf(root)
printtreeditels(root)