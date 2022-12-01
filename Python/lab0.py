class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

root = Node(11)
root.left = Node(22)
root.right = Node(33)
root.left.left = Node(44)
root.left.right = Node(55)
root.right.left = Node(66)
root.right.right = Node(77)

#find the inorder traversal of binary tree
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

print("Inorder traversal of binary tree is:")
inorder(root)

#find the preorder traversal of binary tree
def preorder(root):
    if root:
        print(root.data)
        preorder(root.left)
        preorder(root.right)

print("Preorder traversal of binary tree is:")
preorder(root)

#find the postorder traversal of binary tree
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

def isbalanced(root):
    if root is None:
        return True
    lheight = height(root.left)
    rheight = height(root.right)

    if (abs(lheight - rheight) <= 1) and isbalanced(root.left) is True and isbalanced(root.right) is True:
        return True

    return False

if isbalanced(root):
    print("Tree is balanced")
else:
    print("Tree is not balanced")


def insert(root, data):
    if root is None:
        return Node(data)
    else:
        if root.data == data:
            return root
        elif root.data < data:
            root.right = insert(root.right, data)
        else:
            root.left = insert(root.left, data)
    return root

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

r = None
r = insert(r, 60)
r = insert(r, 12)
r = insert(r, 4)
r = insert(r, 1)
r = insert(r, 41)
r = insert(r, 29)
r = insert(r, 23)
r = insert(r, 37)
r = insert(r, 90)
r = insert(r, 71)
r = insert(r, 84)
r = insert(r, 100)

print("Original Tree")
inorder(r)

r = deleteNode(r, 84)
print("Tree after deleting 84")
inorder(r)

r = deleteNode(r, 29)
print("Tree after deleting 29")
inorder(r)

r = deleteNode(r, 41)
print("Tree after deleting 41")
inorder(r)

def smallest(root):
    if root is None or root.left is None:
        return root
    return smallest(root.left)

print("Smallest element is: ", smallest(r).data)

def kthlargest(root, k):
    if root is None:
        return None
    right = kthlargest(root.right, k)
    if right is not None:
        return right
    k[0] -= 1
    if k[0] == 0:
        return root
    return kthlargest(root.left, k)

k = [3]
res = kthlargest(r, k)
if res is None:
    print("There are less than k nodes in the Tree")
else:
    print("Kth largest element is ", res.data)


def merge(root1, root2):
    if root1 is None:
        return root2
    if root2 is None:
        return root1
    root1.data += root2.data
    root1.left = merge(root1.left, root2.left)
    root1.right = merge(root1.right, root2.right)
    return root1



first_tree = []
f = int(input("Enter the size of first tree : "))
tree1 = None

for i in range(0,f):
    val = int(input("Enter the node : "))
    first_tree.append(val)

for i in range(0,f):
    tree1 = insert(tree1, first_tree[i])

print("The first tree is: ")
inorder(tree1)

second_tree = []
s = int(input("Enter the size of second tree : "))
tree2 = None

for i in range(0,s):
    val = int(input("Enter the node : "))
    second_tree.append(val)

for i in range(0,s):
    tree2 = insert(tree2, second_tree[i])

print("The second tree is: ")
inorder(tree2)

print("The merged tree is ")
inorder(mergeTrees(tree1, tree2))