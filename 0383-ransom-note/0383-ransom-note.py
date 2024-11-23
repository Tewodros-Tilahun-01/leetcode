class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = Counter(magazine)
        for i in ransomNote:
            if i not in count or count[i] == 0 :
                return False
            else:
                count[i] -= 1
        return True