# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prv = None
        while curr:
            nextl = curr.next
            curr.next = prv
            prv = curr
            curr = nextl
        return prv


        

