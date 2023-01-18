
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

class Solution:
    #Function to find first node if the linked list has a loop.
    def findFirstNode(self, head):

        if (head==None or head.next==None):
            return -1

        slowPointer = head
        fastPointer = head
        slowPointer = slowPointer.next
        fastPointer = fastPointer.next.next
        
        #check if loop is there or not
        while(fastPointer and fastPointer.next):
            if(slowPointer==fastPointer):
                break
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
        
        if slowPointer!=fastPointer:
            return -1

        #return the first node of the loop
        slowPointer = head
        while slowPointer!=fastPointer:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next

        return slowPointer.data


s = Solution()
root = Node(1)
root.next = Node(3)
root.next.next = Node(2)
root.next.next.next = Node(4)
root.next.next.next.next = Node(5)
root.next.next.next.next.next = root.next

print(s.findFirstNode(root))