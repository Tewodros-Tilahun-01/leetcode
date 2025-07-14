# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head.next.next:
            return head.val + head.next.val
        max_twin = 0
        fast = head
        slow = head
        stack = []
        while fast and fast.next:
            stack.append(slow.val)
            fast = fast.next.next
            slow = slow.next


        while stack:
            max_twin = max(max_twin ,slow.val + stack.pop())
            slow = slow.next

        return max_twin