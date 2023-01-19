class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


# root = Node(1)
# root.left = Node(12)
# root.right = Node(9)
# root.left.left = Node(5)
# root.left.right = Node(6)

# #preorder traversal of binary tree
# def preorder(root):
#     if root:
#         print(root.data)
#         preorder(root.left)
#         preorder(root.right)

# print("Preorder traversal of binary tree is:")
# preorder(root)

# #inorder traversal of binary tree
# def inorder(root):
#     if root:
#         inorder(root.left)
#         print(root.data)
#         inorder(root.right)

# print("Inorder traversal of binary tree is:")
# inorder(root)

# #postorder traversal of binary tree
# def postorder(root):
#     if root:
#         postorder(root.left)
#         postorder(root.right)
#         print(root.data)

# print("Postorder traversal of binary tree is:")
# postorder(root)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(6)
root.left.right.right = Node(7)

#find the inorder traversal of binary tree
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

print("Inorder traversal of binary tree is:")
inorder(root)

# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.left = Node(6)
# root.right.right = Node(7)

# #find the inorder traversal of binary tree
# def inorder(root):
#     if root:
#         inorder(root.left)
#         print(root.data)
#         inorder(root.right)

# print("Inorder traversal of binary tree is:")
# inorder(root)