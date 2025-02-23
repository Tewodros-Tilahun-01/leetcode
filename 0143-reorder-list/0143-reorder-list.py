# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        list1 = []
        temp = head
        while temp:
            list1.append(temp)
            temp = temp.next
        left = 0
        right = len(list1)-1
        while left < right: 
            list1[left].next = list1[right]
            left += 1
            list1[right].next = list1[left]
            right -= 1
            list1[left].next = None
            
