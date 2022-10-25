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

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

