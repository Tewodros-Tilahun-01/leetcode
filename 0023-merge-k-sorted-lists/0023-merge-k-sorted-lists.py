# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = ListNode(-1)
        temp  = dummy
        for head in lists:
            while head:
                heapq.heappush(heap,head.val)
                head = head.next
        while heap:
            val = heapq.heappop(heap)
            temp.next = ListNode(val)
            temp = temp.next
        return dummy.next