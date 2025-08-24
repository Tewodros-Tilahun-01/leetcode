class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        ref = set(list(allowed))
        for word in words:
            allow = True
            for letter in word:
                if letter not in ref:
                    allow = False
                    break
            if allow:count += 1
        return count