class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        graph = {}
        alph  = "abc def ghi jkl mno pqrs tuv wxyz"
        alphList = alph.split(" ")
        for i in range(2,10):
            graph[i] = list(alphList[i-2])
        def backtrack(string , digits ,graph , res):

            if len(digits) == 0:
                if string:res.append(string)
                return

            key = int(digits[0])
            for ch in graph[key]:
                backtrack(string + ch, digits[1:] ,graph , res)

        res = []
        backtrack("",list(digits), graph , res)
        return res