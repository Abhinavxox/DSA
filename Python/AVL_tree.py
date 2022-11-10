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

#insert node
def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    balance = balancedFactor(root)
    if balance > 1 and data < root.left.data:
        return right_rotation(root)
    if balance < -1 and data > root.right.data:
        return left_rotation(root)
    if balance > 1 and data > root.left.data:
        return left_right_rotation(root)
    if balance < -1 and data < root.right.data:
        return right_left_rotation(root)
    return root

print("Enter the elements to be inserted in the AVL tree: ")
elements = input().split()
root = Node(elements[0])
for i in range(1, len(elements)):
    root.insert(elements[i])

def balancedFactor(root):
    if root is None:
        return 0
    return height(root.left) - height(root.right)

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



def delete(root, data):
    if root is None:
        return root
    elif data < root.data:
        root.left = delete(root.left, data)
    elif data > root.data:
        root.right = delete(root.right, data)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = minValueNode(root.right)
        root.data = temp.data
        root.right = delete(root.right, temp.data)
    if root is None:
        return root
    root.height = 1 + max(height(root.left), height(root.right))
    balance = balancedFactor(root)
    if balance > 1 and balancedFactor(root.left) >= 0:
        return right_rotation(root)
    if balance < -1 and balancedFactor(root.right) <= 0:
        return left_rotation(root)
    if balance > 1 and balancedFactor(root.left) < 0:
        root.left = left_rotation(root.left)
        return right_rotation(root)
    if balance < -1 and balancedFactor(root.right) > 0:
        root.right = right_rotation(root.right)
        return left_rotation(root)
    return root

def minValueNode(node):
    current = node
    while(current.left is not None):
        current = current.left
    return current

deletionValue = input("Enter the node you want to delete :")
delete(root, deletionValue)
print("Inorder traversal of binary tree after deletion of "+deletionValue+" is : ")
inorder(root)
print("The height of the tree after deletion is : ",height(root)-1)
