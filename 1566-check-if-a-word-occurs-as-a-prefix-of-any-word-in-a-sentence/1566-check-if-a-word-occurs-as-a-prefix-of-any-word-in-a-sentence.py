class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        def isPrefix(word,serchword):
            if len(word) < len(serchword):
                return False
            for pt1 in range(len(searchWord)):
                if word[pt1] != serchword[pt1]:
                    return False
            return True
        sentence = sentence.split()
        for i in range(len(sentence)):
            if isPrefix(sentence[i] ,searchWord):
                return i+1
        return -1