class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        pt1 , pt2 = 0 , 0 
        count = 0
        g.sort()
        s.sort()
        while pt1 < len(g) and pt2 < len(s):
            if g[pt1] <= s[pt2]:
                count += 1
                pt1 += 1
                pt2 += 1
            else:
                pt2 += 1

        return count
            