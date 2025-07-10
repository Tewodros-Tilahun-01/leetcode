class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        
class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        count = 0
        temp = self.head
        while temp:
            if count == index:
                return temp.val
            count += 1
            temp = temp.next
        return -1
        

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(val)
      

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            newNode = Node(val)
            newNode.next = self.head
            self.head = newNode
            return

        cur = self.head
        for _ in range(index):
            prv = cur 
            if cur:
                cur = cur.next
            else:
                return
        if prv:
            prv.next = Node(val)
            prv.next.next = cur
        
        

    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return 
        if index == 0 and self.head:
            self.head = self.head.next
        

        cur = self.head
        prv = None

        for _ in range(index):
            prv = cur 
            if cur:
                cur = cur.next
            else:
                return
        if prv and prv.next:
            prv.next = prv.next.next
        
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)