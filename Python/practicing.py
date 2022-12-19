#heap

def insert(heap,data):
    heap.append(data)
    i = len(heap)-1
    while(i>0):
        parent = i//2
        if heap[parent]<heap[i]:
            heap[parent],heap[i] = heap[i],heap[parent]
        else:
            break

def delete(heap,data):
    n = len(heap)-1
    heap[0] = heap[n]
    n = n-1
    i = 0
    while(i<n):
        l = heap[2*i]
        r = heap[2*i + 1]
        larger = 2*i if l>r else 2*i+1
        if heap[i]<heap[larger]:
            heap[larger],heap[i] = heap[i],heap[larger]
        else:
            break
    
def heapify(heap,n,i):
    largest = i
    l = 2*i+1
    r = 2*i+2

    if l<n and heap[l]>heap[largest]:
        largest = l
    if r<n and heap[r]>heap[largest]:
        largest = r

    if largest!=i:
        heap[largest],heap[i] = heap[i],heap[largest]
        heapify(heap,n, largest)

def buildheap(heap, n):
    for i in range(n,-1,-1):
        heapify(heap,n,i)
    
heap = [10,30,50,20,35,15]
buildheap(heap,6)
print(heap)


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

root = Node(4)
root.insert(2)
root.insert(6)
root.insert(1)
root.insert(3)
root.insert(5)
root.insert(7)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

print("the bst is : ")
inorder(root)


arr = []
global i 
i = 0
def arrayApp(root):
    if root:
        arrayApp(root.left)
        arr.append(root.data)
        arrayApp(root.right)

arrayApp(root)
print(arr)

def convert(root):
    global i

    if root is None:
        return root

    root.left = convert(root.left)
    root.right = convert(root.right)
    root.data = arr[i]

    i = i+1
    return root

convert(root)
print("After convert")

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data)

postorder(root)
