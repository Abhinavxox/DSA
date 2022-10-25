class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        #if tree is not empty
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
        #if tree is empty
        else:
            self.data = data

#find the inorder traversal of binary tree
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

# print("Inorder traversal of binary tree is:")
# inorder(root)

#find the preorder traversal of binary tree
def preorder(root):
    if root:
        print(root.data)
        preorder(root.left)
        preorder(root.right)

# print("Preorder traversal of binary tree is:")
# preorder(root)

#find the postorder traversal of binary tree
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data)

# print("Postorder traversal of binary tree is:")
# postorder(root)

#determine if a binary tree is height balnced or not
def isHeightBalanced(root):
    if root == None:
        return True
    lh = height(root.left)
    rh = height(root.right)
    if abs(lh-rh) <= 1 and isHeightBalanced(root.left) and isHeightBalanced(root.right):
        return True
    return False

#find the height of a binary tree
def height(root):
    if root == None:
        return 0
    return 1 + max(height(root.left), height(root.right))

# print(isHeightBalanced(root))

#insert into a binary search tree 10 values
root = Node(10)
root.insert(5)
root.insert(15)
root.insert(3)
root.insert(7)
root.insert(12)
root.insert(18)
root.insert(1)
root.insert(4)
root.insert(6)

# print("Inorder traversal of binary tree is:")
# inorder(root)






