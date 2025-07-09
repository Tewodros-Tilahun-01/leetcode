# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = None
        if not head:return dummy
        def rec(node):
            nonlocal dummy
            if node.next == None :
                dummy = node
                return node      
            next = rec(node.next)     
            node.next = None
            next.next = node
            return next.next
        rec(head)
        return dummy