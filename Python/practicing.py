#for avl trees
class Node:

    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left == None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right == None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    
def left_rotation(root):
    new_node = root.right
    root.right = new_node.left
    new_node.left = root
    return new_node

def right_rotation(root):
    new_node = root.left
    root.left = new_node.right
    new_node.right = root
    return new_node

def left_right_rotation(root):
    root.left = left_rotation(root.left)
    return right_rotation(root)

def right_left_rotation(root):
    root.right = right_rotation(root.right)
    return left_rotation(root)

