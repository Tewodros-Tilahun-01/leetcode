class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def dfs(pair ,open,close):
            nonlocal valid
            if open + close == 2 * n:
                valid.append(pair)
                return 
            if open < n:
                dfs(pair + "(",open+1,close)
            if close < open:
                dfs(pair + ")", open , close + 1)        
        valid = []
        dfs("",0,0)
        return valid