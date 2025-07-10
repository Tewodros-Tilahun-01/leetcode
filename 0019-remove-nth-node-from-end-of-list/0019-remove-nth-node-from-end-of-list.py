# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1,head)
        def rec(node,rem):
            if not node:
                return rem
            rem = rec(node.next,rem) - 1
            if rem == 0:
                node.next = node.next.next
            return rem
        rec(dummy,n+1)
        return dummy.next
            
