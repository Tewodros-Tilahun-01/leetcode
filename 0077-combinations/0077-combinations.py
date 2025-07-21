class Solution:
    def combine(self,n,k):
        
        
        def backtrack(com,res,start):
            if len(com) == k:
                res.append(com[:])
                return 
            for i in range(start,n+1):
                com.append(i)
                backtrack(com,res,i+1)
                com.pop()
        res = []
        backtrack([],res,1)

        return res