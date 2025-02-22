# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tchel = head
        eli = head
        while tchel and tchel.next:
            eli = eli.next
            tchel = tchel.next.next
            if eli == tchel:
                return True
        return False 
            
            