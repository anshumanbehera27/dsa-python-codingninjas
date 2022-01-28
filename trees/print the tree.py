class BinaryTreesnode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def printtree(root):
    if root == None:
        return
    print(root.data)
    printtree(root.left)
    printtree(root.right)
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

bt1 = BinaryTreesnode(1)
bt2 = BinaryTreesnode(2)
bt3 = BinaryTreesnode(3)
bt4 = BinaryTreesnode(4)

bt5 = BinaryTreesnode(5)
bt1.left = bt2
bt1.right = bt3
bt2.left = bt4
bt2.right = bt5
printtreeditels(bt1)




