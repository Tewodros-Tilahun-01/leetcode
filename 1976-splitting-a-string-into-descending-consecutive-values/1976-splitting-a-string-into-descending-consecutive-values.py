class Solution:
    def splitString(self, s: str) -> bool:
        
        def solve(i, x): 
            
            if i == len(s):
                return True 
            if x == 0: 
                return False 
            res = False 
            for j in range(i, len(s) - int(i == 0)):
                if x is None or int(s[i:j+1]) == x - 1: 
                    res = res or solve(j+1, int(s[i:j+1]))
                    
            return res 
        
        return solve(0, None)