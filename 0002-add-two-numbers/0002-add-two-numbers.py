# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
       
        list1 = []
        list2 = []
        while l1:
            list1.append(l1.val)
            l1 = l1.next
        while l2:
            list2.append(l2.val)
            l2 = l2.next
        res = 0
        x = 1
        for i in list1:
            res += x * i
            x = x * 10
        x = 1
        for i in list2:
            res += x * i
            x = x * 10
        x = 10
        list1 = []
        head = None
        if res == 0:
            head = ListNode(0)
        while res > 0:
            temp = res % x 
            list1.append(temp)
            res = (res - temp)//10
        list1.reverse()
       
        for i in list1:
            temp = ListNode(i,head)
            head = temp
        return head


        
        