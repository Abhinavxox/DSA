# question 1
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

# question 2
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

# question 3
# import math
# N = int(input("Enter the value of N : "))
# arr = []
# for i in range(N):
#     arr.append(int(input("Enter the element "+str(i)+" : ")))
# def height(arr):
#     return int(math.log(N,2))
# print(height(arr))

# question 4