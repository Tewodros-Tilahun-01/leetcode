# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rec(node):
            if not node:return
            if node.next and node.val == node.next.val:
                node.next = node.next.next
                rec(node)
            elif node.next:
                rec(node.next)
        rec(head)
        return head