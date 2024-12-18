class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        for word in words:
            j = 0
            if len(word) == len(pattern):
                pt = {}
                set1 = set()
                while j<len(word):
                    if not pattern[j] in pt :
                        if word[j] in set1:
                            break
                        pt[ pattern[j] ] = word[j] 
                        set1.add(word[j])    
                    elif pt[ pattern[j] ] != word[j]:
                        break
                    j += 1
                if j == len(word):
                    res.append(word)
        return res
                        
