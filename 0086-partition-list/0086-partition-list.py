# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:return head
        head = ListNode(-1,head)
        cur = head
        prv = None
        while cur.next:
            if not prv and cur.next.val >= x:
                prv = cur
            elif prv and cur.next.val < x:
                nex = prv.next
                prv.next = cur.next
                cur.next = cur.next.next
                prv.next.next = nex
                prv = prv.next
            else:
                cur = cur.next
        return head.next
            
