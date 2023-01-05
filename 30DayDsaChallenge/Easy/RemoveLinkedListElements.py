# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        pointer = head
        while(pointer.next!=None):
            if pointer==head and pointer.val == val:
                head = pointer.next
            if pointer.next.val == val:
                pointer.next = pointer.next.next
            pointer = pointer.next
