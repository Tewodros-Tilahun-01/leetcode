# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if right <= 1:return head
        temp = ListNode(0,head)
        dummy = temp
        temp = dummy
        pos = 0
        prv = None
        nxt = None
        flag = False
        while temp:
            cur = temp
            while pos >= left and pos <= right:
                nxt = cur.next
                cur.next = prv
                prv = cur
                cur = nxt
                pos += 1
                flag = True
            if flag:
                temp.next.next = None
                temp.next = None
                temp.next = cur
                break
            else:
                prv = temp
                temp = temp.next
                pos +=1
        temp = dummy
        while dummy.next:
            dummy = dummy.next
        dummy.next = prv
        return temp.next

            
        
                
            
        
           


        