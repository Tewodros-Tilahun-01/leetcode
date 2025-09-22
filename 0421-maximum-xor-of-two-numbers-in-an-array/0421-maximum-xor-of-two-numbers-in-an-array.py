class Node:
    def __init__(self):
        self.kids = [None, None]  # 0 and 1

class Solution:
    def findMaximumXOR(self, arr: List[int]) -> int:
        root = Node()
        
        for n in arr:
            cur = root
            for i in range(31, -1, -1):
                b = (n >> i) & 1
                if not cur.kids[b]:
                    cur.kids[b] = Node()
                cur = cur.kids[b]
        
        # Query for maximum XOR
        ans = 0
        for n in arr:
            cur = root
            val = 0
            for i in range(31, -1, -1):
                b = (n >> i) & 1
                t = 1 - b
                if cur.kids[t]:
                    val |= (1 << i)
                    cur = cur.kids[t]
                else:
                    cur = cur.kids[b]
            ans = max(ans, val)
        
        return ans