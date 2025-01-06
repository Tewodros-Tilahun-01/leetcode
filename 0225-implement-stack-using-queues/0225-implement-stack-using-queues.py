class MyStack:

    def __init__(self):
        self.head = None

    def push(self, x: int) -> None:
        newNode = Node(x)
        newNode.next = self.head
        self.head = newNode

    def pop(self) -> int:
        res = self.head.data
        self.head = self.head.next
        return res

    def top(self) -> int:
        return self.head.data


    def empty(self) -> bool:
        return not self.head

class Node:
    def __init__(self,x):
        self.next = None
        self.data = x


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()