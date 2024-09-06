class BrowserHistory:
    
    def __init__(self, homepage: str):
       self.head = node(homepage) 
        
    def visit(self, url: str) -> None:
        temp = node(url)
        self.head.prv = temp
        temp.next = self.head 
        self.head = temp

    def back(self, steps: int) -> str:
        while steps > 0 and self.head.next != None:
            self.head = self.head.next
            steps -= 1
        return self.head.data

    def forward(self, steps: int) -> str:
        while steps > 0 and  self.head.prv != None:
            self.head = self.head.prv
            steps -= 1
        return self.head.data
class node:
    next = None
    prv = None
    def __init__ (self,data):
        self.data = data

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)