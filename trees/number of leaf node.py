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

def numberofleef(root):
    if root == None :
        return 0
    if root.left == None and root.right == None:
        return 1
    numofleft = numberofleef(root.left)
    numofright = numberofleef(root.right)
    return numofleft + numofright




root = takeInput()
printtreeditels(root)
print("number of leef are ",numberofleef(root))