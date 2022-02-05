class bstNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def printBST(root):
    if root.left is not None:
        printBST(root.left)
    print(root.data)
    if root.right is not None:
        printBST(root.right)
    
    

def bstInsert(root, data):
    if root is None:
        return bstNode(data)
    elif root.data < data:
        root.right = bstInsert(root.right, data)
    elif root.data > data:
        root.left = bstInsert(root.left, data)
    return root


bst = bstNode(5)
bstInsert(bst, 4)
bstInsert(bst, 9)
bstInsert(bst, 6)
printBST(bst)


        
        