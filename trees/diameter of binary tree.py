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
def height(root):
    if root == None:
        return 0
    return 1 + max(height(root.left),height(root.right))

def isbalanced(root):
    if root == None:
        return True
    lh = height(root.left)
    rh = height(root.right)
    if (lh - rh > 1 or rh - lh > 1 ):
        return False
    isleftbalanced = isbalanced(root.left)
    isrightbalanced = isbalanced(root.right)
    if isleftbalanced and isrightbalanced:
        return True
    else:
        return False
def dimaterofthe(root):
    if root == None :
        return 0
    if isbalanced == True :
       lh = height(root.left)
       rh = height(root.right)
       return  1+ lh + rh
    elif (max(lh,rh) == lh ):
       lh = height(root.left)
       return 1 + lh
    elif :
       rh = height(root.right)
       return 1 + rh









root = takeInput()
print(dimaterofthe(root))
printtreeditels(root)