class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        firstRow = set("qwertyuiop")
        secondRow = set("asdfghjkl")
        thirdRow = set("zxcvbnm")
        res = []
        def valid(word,s):
            for l in word:
                if l.lower() not in s:
                    return False
            return True

        for word in words:
            first = word[0].lower()
            if first in firstRow:
                if valid(word,firstRow):res.append(word)
            elif first in secondRow:
               if valid(word,secondRow):res.append(word)
            else:
                if valid(word,thirdRow):res.append(word)
        return res

