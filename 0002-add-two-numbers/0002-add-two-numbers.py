# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x = 10
        list1 = []
        resHead = None

        res = self.add(l1,1)
        res += self.add(l2,1)
        
        if res == 0:
            resHead = ListNode(0)
        while res > 0:
            temp = res % x 
            list1.append(temp)
            res = (res - temp)//10
        list1.reverse()
       
        for i in list1:
            temp = ListNode(i,resHead)
            resHead = temp
        return resHead

    def add(self,head,x):
        if head == None:
            return 0
        temp = self.add(head.next,x*10)
        return temp + (head.val * x)
        
        