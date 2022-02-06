#basic BST implimentation
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
        root = bstNode(data)
    elif root.data < data:
        root.right = bstInsert(root.right, data)
    elif root.data > data:
        root.left = bstInsert(root.left, data)
    return root

def bstSearch(root, val):
    def wrapper(root, val):
        if root is None:
            return ("X")
        elif root.data < val:
            return "R"+str(wrapper(root.right, val))
        elif root.data > val:
            return "L"+str(wrapper(root.left, val))
        elif root.data == val:
            return root.data
    return [x for x in wrapper(root, val)]

bst = bstNode(5)
bstInsert(bst, 4)
bstInsert(bst, 9)
bstInsert(bst, 6)
printBST(bst)
print(bstSearch(bst, 7))
print(bstSearch(bst, 6))


        
        