class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        newWord = ""
        for word in words:
            newWord += word
            if s == newWord:
                return True
        return False