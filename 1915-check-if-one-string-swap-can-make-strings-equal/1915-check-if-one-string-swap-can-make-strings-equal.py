class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        count = 0
        set1 = set()
        set2 = set()
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
                set1.add(s1[i])
                set2.add(s2[i])
        if count not in [0,2] or set1 != set2:
            return False
        else:
            return True