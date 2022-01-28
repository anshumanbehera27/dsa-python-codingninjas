def elementsInRangeK1K2(root, k1, k2):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    if root == None:
        return


    if root.data > k2 :
         elementsInRangeK1K2(root.left, k1, k2)
    elif root.data < k1:
         elementsInRangeK1K2(root.right, k1, k2)
    else:

        elementsInRangeK1K2(root.left, k1, k2)
        print(root.data) # we have to write the print here because i have to print the node in incresing order
        elementsInRangeK1K2(root.right, k1, k2)
