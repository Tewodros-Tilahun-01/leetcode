# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:  
        res = []
        def rec(node,total,pow):
            if not node:
                return total
            total += node.val * pow
            return rec(node.next,total,pow * 10)
        x = rec(l1,0,1) + rec(l2,0,1)
        head = ListNode(0)
        temp = head
        if x == 0:
            return ListNode(x)
        while x != 0:
            val = x%10
            x = x//10
            temp.next = ListNode(val)
            temp = temp.next
        return head.next
