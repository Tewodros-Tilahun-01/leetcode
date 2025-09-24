class MapSum:

    def __init__(self):
        self.children = [None] * 26
        self.val = None

    def change_to_index(self,s:str):
        return ord(s) - ord("a")

    def insert(self, key: str, val: int) -> None:
        node = self
        for c in key:
            index = self.change_to_index(c)
            print(node)
            if not node.children[index]:
                node.children[index] = MapSum()
            node = node.children[index]
        node.val = val
        
    def dfs(self,s:str):
        if not s:
            return 0  
        val = 0
        if s.val:val += s.val
        for c in  s.children:
            val += self.dfs(c)
        return val


    def sum(self, prefix: str) -> int:
        node = self
        val = 0
        for c in prefix:
            index = self.change_to_index(c)
            if not node.children[index]:
                return 0
            node = node.children[index]
        if node.val:
            val += node.val
        for c in node.children:
            if c:
                val += self.dfs(c)
        return val

        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)