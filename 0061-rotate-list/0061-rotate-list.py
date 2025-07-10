# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        count = 0
        temp = head
        while temp:
            temp = temp.next
            count += 1
        k = k % count
        rotate = count - k -1
        temp = head
        
        if k == 0:
            return head

        for _ in range(rotate):
            temp = temp.next
        
        lastOne = temp.next
        newHead = lastOne
        temp.next = None

        while lastOne.next:
            lastOne = lastOne.next
        lastOne.next = head
        return newHead


        
