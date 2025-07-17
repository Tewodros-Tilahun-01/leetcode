class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        swap = 0
        hashmap1 = set()
        hashmap2 = set()

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                swap += 1
                hashmap1.add(s1[i])
                hashmap2.add(s2[i])
        if swap == 2 and hashmap1 == hashmap2:
            return True
        return False
