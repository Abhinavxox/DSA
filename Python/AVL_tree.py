#Build a AVL tree, write separate function for each rotation. You need to get the elements to be inserted from the user.
# After construction of the tree, return the height of the tree.
# Write a function to delete the nodes from the tree. Elements to be deleted as per user’s wish. 
# Return the heightof tree after each deletion.

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left == None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right == None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

#left rotation
def left_rotation(node):
    new_node = node.right
    node.right = new_node.left
    new_node.left = node
    return new_node

#right rotation
def right_rotation(node):
    new_node = node.left
    node.left = new_node.right
    new_node.right = node
    return new_node

#left-right rotation
def left_right_rotation(node):
    node.left = left_rotation(node.left)
    return right_rotation(node)

#right-left rotation
def right_left_rotation(node):
    node.right = right_rotation(node.right)
    return left_rotation(node)

#question 1

print("Enter the elements to be inserted in the AVL tree: ")
elements = input().split()
root = Node(elements[0])
for i in range(1, len(elements)):
    root.insert(elements[i])

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

print("Inorder traversal of binary tree is:")
inorder(root)

def preorder(root):
    if root:
        print(root.data)
        preorder(root.left)
        preorder(root.right)

print("Preorder traversal of binary tree is:")
preorder(root)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data)

print("Postorder traversal of binary tree is:")
postorder(root)

def height(root):
    if root is None:
        return 0
    else:
        lheight = height(root.left)
        rheight = height(root.right)

        if lheight > rheight:
            return lheight+1
        else:
            return rheight+1
        
print("The height of the tree created is : ",height(root)-1)


def deleteNode(root, data):
    if root is None:
        return root
    if data < root.data:
        root.left = deleteNode(root.left, data)
        return root
    elif data > root.data:
        root.right = deleteNode(root.right, data)
        return root
    if root.left is None and root.right is None:
        return None
    if root.left is None:
        temp = root.right
        root = None
        return temp
    elif root.right is None:
        temp = root.left
        root = None
        return temp
    
    succParent = root
    succ = root.right
    while succ.left is not None:
        succParent = succ
        succ = succ.left
    if succParent != root:
        succParent.left = succ.right
    else:
        succParent.right = succ.right
    root.data = succ.data
    return root

deletionValue = int(input("Enter the node you want to delete"))
deleteNode(root, deletionValue)
print("The height of the tree after deletion is : ",height(root)-1)
