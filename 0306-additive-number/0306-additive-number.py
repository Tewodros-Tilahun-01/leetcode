class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        
        def backtrack(path,i):
            if i == len(num) and len(path) > 2:
                return True
            
            for j in range(i,len(num)):
                val = num[i:j+1]
                if (val[0] != "0" or len(val) == 1):
                    if len(path) < 2 or path[-1] + path[-2] == int(val):
                        path.append(int(val))
                        if backtrack(path,j+1):
                            return True
                        path.pop()
            return False
        return backtrack([],0)           


        
            