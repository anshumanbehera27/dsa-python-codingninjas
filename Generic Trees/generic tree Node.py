class TreeNode :
    def __init__(self,data):
        self.data = data
        self.children = list()
def printTree(root):
    # this is not a base case it  is a edge case
    if root == None :
        return
    print(root.data)
    for child in root.children:
        printTree(child)
def printTreeDetailed(root):
    if root == None :
        return
    print(root.data , ":" , end = " ")
    for child in root.children:
        print(child.data , "," , end = "")
    print()
    for child in root.children:
        printTreeDetailed(child)
def takeTreeInput():
    print("Enter root Data")
    rootData  = int(input())
    if rootData == -1 :
        return None
    root = TreeNode(rootData)
    print("enter the number of children " , rootData)
    childrenCount = int(input())
    for i in range (childrenCount):
        child = takeTreeInput()
        root.children.append(child)
    return root

root = takeTreeInput()
# print the simple tree
#printTree(n1)

 # print the detiled tree
printTreeDetailed(root)

