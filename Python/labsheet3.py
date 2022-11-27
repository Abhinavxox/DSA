class Node:

    def __init__(self,data):
        self.right = None
        self.left = None
        self.data = data

root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)
# root.right.right.right = Node(8)
# root.right.right.right.right = Node(9)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

inorder(root)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data)

postorder(root)

def preorder(root):
    if root:
        print(root.data)
        preorder(root.left)
        preorder(root.right)

preorder(root)

#function to calculate the height
def height(root):
    if root==None:
        return 0

    lheight = height(root.left) 
    rheight = height(root.right)

    if lheight>rheight:
        return lheight+1
    else:
        return rheight+1

print("the height of tree is", height(root))


#check is the tree is height balanced
def isBalanced(root):
    if root==None:
        return True
    lheight = height(root.left) 
    rheight = height(root.right)

    if(abs(lheight-rheight)<=1 and isBalanced(root.left) and isBalanced(root.right)):
        return True
    else:
        return False

print("the tree is balanced? ", isBalanced(root))