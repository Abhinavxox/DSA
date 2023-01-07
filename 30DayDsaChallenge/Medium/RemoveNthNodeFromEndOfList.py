# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next==None:
            return head.next
        pointer = head
        counter = 1
        while pointer.next!=None:
            counter+=1
            pointer = pointer.next
        position = counter-n
        if position ==0:
            return head.next
        pointer = head
        while pointer.next!=None:
            if position==1:
                temp = pointer.next
                pointer.next = temp.next
                return head
            position -=1
            pointer = pointer.next

s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head = s.removeNthFromEnd(head,2)
while head!=None:
    print(head.val)
    head = head.next
    