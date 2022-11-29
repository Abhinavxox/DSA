# class Node:

#     def __init__(self,data):
#         self.right = None
#         self.left = None
#         self.data = data

# root = Node(4)
# root.left = Node(2)
# root.right = Node(6)
# root.left.left = Node(1)
# root.left.right = Node(3)
# root.right.left = Node(5)
# root.right.right = Node(7)
# # root.right.right.right = Node(8)
# # root.right.right.right.right = Node(9)

# def inorder(root):
#     if root:
#         inorder(root.left)
#         print(root.data)
#         inorder(root.right)

# inorder(root)

# def postorder(root):
#     if root:
#         postorder(root.left)
#         postorder(root.right)
#         print(root.data)

# postorder(root)

# def preorder(root):
#     if root:
#         print(root.data)
#         preorder(root.left)
#         preorder(root.right)

# preorder(root)

# #function to calculate the height
# def height(root):
#     if root==None:
#         return 0

#     lheight = height(root.left) 
#     rheight = height(root.right)

#     if lheight>rheight:
#         return lheight+1
#     else:
#         return rheight+1

# print("the height of tree is", height(root))


# #check is the tree is height balanced
# def isBalanced(root):
#     if root==None:
#         return True
#     lheight = height(root.left) 
#     rheight = height(root.right)

#     if(abs(lheight-rheight)<=1 and isBalanced(root.left) and isBalanced(root.right)):
#         return True
#     else:
#         return False

# print("the tree is balanced? ", isBalanced(root))

class Node:
    
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    
    def insert(self,data):
        if self.data is None:
            self.data = data
        else:
            if data<self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

    def delete(self,data):
        if self is None:
            return self


        if data < self.data:
            self.left = self.left.delete(data)
            return self
        elif data > self.data:
            self.right = self.right.delete(data)
            return self

        if self.left is None and self.right is None:
            return None
        
        #case-1 only leaf node no children  
        if self.left is None:
            temp = self.right 
            self = None
            return temp
        elif self.right is None:
            temp = self.left
            self = None
            return temp
        
        #case2
        succParent = self
        succ = self.right
        while succ.left is not None:
            succParent = succ
            succ = succ.left
        
        if succParent != self:
            succParent.left = succParent.right
        else:
            succParent.right = succParent.right
        
        self.data = succ.data
        return self



#inserting 10 values in 

root = Node(60)
root.insert(12)
root.insert(90)
root.insert(4)                
root.insert(41)
root.insert(71)
root.insert(100)
root.insert(1)
root.insert(29)
root.insert(23)
root.insert(37)
root.insert(84)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

print("the bst is : ")
inorder(root)

#function to delete a node
root.delete(84)
print("\nthe bst after deleting 84 is : ")
inorder(root)