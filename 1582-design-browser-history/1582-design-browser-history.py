class BrowserHistory:
    
    def __init__(self, homepage: str):
      
        obj = Node(homepage)
        self.head = obj

    def visit(self, url: str) -> None:
        obj = Node(url)
        obj.nextpr = self.head
        self.head.prvpr = obj   
        self.head = obj
        
    def back(self, steps: int) -> str:
        temp = self.head
        for i in range(0,steps):
            if temp.nextpr == None:
                break
            temp = temp.nextpr
        self.head = temp
        return temp.data

    def forward(self, steps: int) -> str:
        temp = self.head
        for i in range(0,steps):
            if temp.prvpr == None:
                break
            temp = temp.prvpr
        self.head = temp
        return temp.data
    
class Node:    
    data = None
    nextpr = None
    prvpr = None
    def __init__(self,data:str):
        self.data = data
    

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)