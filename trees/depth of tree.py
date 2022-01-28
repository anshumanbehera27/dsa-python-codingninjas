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

def depthofthetree(root,k ):
    if root == None :
        return
    if k == 0 :
        print(root.data)
        return
    depthofthetree(root.left,k-1)
    depthofthetree(root.right, k-1)
def depthoftreewithnode(root,k,d=0):
    if root == None :
        return
    if k == d :
        print(root.data)
        return
    depthoftreewithnode(root.left,k ,d+1 )
    depthoftreewithnode(root.right,k  ,d+1 )






root = takeInput()
printtreeditels(root)
print("depth of thr node is ",depthoftreewithnode(root,2 ))
