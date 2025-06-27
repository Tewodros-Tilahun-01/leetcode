class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        ref = defaultdict(int)
        for ui , vi in edges:
            ref[ui] += 1
            ref[vi] += 1
            if ref[vi] == len(edges)-1:
                return vi
            elif ref[ui] == len(edges)-1:
                return ui