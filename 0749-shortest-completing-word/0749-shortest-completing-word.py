class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        count = {}
        min_len= 100*100
        res = ''
        for i in licensePlate:
            if i.isalpha():
                i = i.lower()
                if i not in count:
                    count[i] = 1
                else:
                    count[i] += 1
        for i in words:
            completing = True
            for j in count:
                if j not in i or i.count(j) < count[j]:
                    completing = False
            if completing and min_len > len(i):
                res = i
                min_len = len(i)
        return res
                
            
        