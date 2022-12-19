# # question 1
# N = int(input("Enterh the value of N : "))
# K = int(input("Enter the value of K : "))
# arr = []
# for i in range(N):
#     arr.append(int(input("Enter the element "+str(i)+" : ")))

# def findKLargest(arr,K):
#     #first sort
#     output_string = ""
#     arr.sort(reverse=True)
#     for i in range(0,K):
#         output_string += " " 
#         output_string +=  str(arr[i])
#     return output_string

# print(findKLargest(arr,K))

# # question 2
# N = int(input("Enter the value of N : "))
# #implement heap sort
# def heapify(arr, n, i):
#     largest = i
#     l = 2 * i + 1
#     r = 2 * i + 2
#     if l < n and arr[i] < arr[l]:
#         largest = l
#     if r < n and arr[largest] < arr[r]:
#         largest = r
#     if largest != i:
#         arr[i], arr[largest] = arr[largest], arr[i]
#         heapify(arr, n, largest)
    
# def buildHeap(arr):
#     n = len(arr)
#     for i in range(n, -1, -1):
#         heapify(arr, n, i)
#     for i in range(n-1, 0, -1):
#         arr[i], arr[0] = arr[0], arr[i]
#         heapify(arr, i, 0)
#     return arr

# arr = []
# for i in range(N):
#     arr.append(int(input("Enter the element "+str(i)+" : ")))
# print(buildHeap(arr))

# #question 3
# import math
# N = int(input("Enter the value of N : "))
# arr = []
# for i in range(N):
#     arr.append(int(input("Enter the element "+str(i)+" : ")))
# def height(arr):
#     return int(math.log(N,2))
# print(height(arr))

#question 4
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

