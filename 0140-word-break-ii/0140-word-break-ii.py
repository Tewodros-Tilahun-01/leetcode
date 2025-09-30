class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordset = set(wordDict)
        res = []

        def backtrack(i,j,arr):
            nonlocal wordset , s ,res 
            if j == i == len(s):
                res.append(" ".join(arr))
                return 
            if j == len(s):
                return
            word = s[i:j+1]
            if word in wordset:
                arr.append(word)
                backtrack(j+1,j+1,arr)
                arr.pop()  
            backtrack(i,j+1,arr)
        backtrack(0,0,[])
        return res