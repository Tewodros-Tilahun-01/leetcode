class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        incoming = set()
        res = []
        for edge in edges:
            incoming.add(edge[1])
        return [i for i in range(n) if i not in incoming]

