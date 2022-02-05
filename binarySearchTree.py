class bstNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def printBST(root):
    if root is not None:
        if root.left is not None:
            printBST(root.left)
        elif root.right is not None:
            printBST(root.right)
        return print(root.data)

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
printBST(bst)


        
        