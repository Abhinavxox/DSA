class Node:
    
    #initialization 
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


#creating and inserting nodes
root = Node(69)
root.insert(70)
root.insert(13)
root.insert(45)
root.insert(23)
root.insert(12)
root.insert(15)
root.insert(16)
root.insert(17)
root.insert(18)


#check whether binary tree is full or not
def isFullTree(root):
    if root == None:
        return True
    if root.left == None and root.right == None:
        return True
    if root.left != None and root.right != None:
        return (isFullTree(root.left) and isFullTree(root.right))
    return False

# print(isFullTree(root))

#check whether binary tree is perfect or not
def isPerfectTree(root):
    if root == None:
        return True
    if root.left == None and root.right == None:
        return True
    if root.left != None and root.right != None:
        return (isPerfectTree(root.left) and isPerfectTree(root.right))
    return False

# print(isPerfectTree(root))

#find the preorder traversal of binary tree
def preorder(root):
    if root:
        print(root.data)
        preorder(root.left)
        preorder(root.right)

# print("Preorder traversal of binary tree is:")
# preorder(root)

#find the inorder traversal of binary tree
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

print("Inorder traversal of binary tree is:")
inorder(root)

#find the postorder traversal of binary tree
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data)

# print("Postorder traversal of binary tree is:")
# postorder(root)

def isCompleteTree(root):
    if root == None:
        return True
    if root.left == None and root.right == None:
        return True
    if root.left != None and root.right != None:
        return (isCompleteTree(root.left) and isCompleteTree(root.right))
    return False