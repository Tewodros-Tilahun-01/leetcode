class Solution:
    def repeatedCharacter(self, s: str) -> str:
        single = set()
        for i in s:
            if i in single:
                return i
            else:
                single.add(i)