class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(target,res,comb):
            if target < 0:
                return 
            if target == 0:
                res.append(comb[:])
                return 
            for val in candidates:
                if comb and val < comb[-1]:
                    continue
                comb.append(val)
                backtrack(target - val , res , comb)
                comb.pop()
            
        res = []
        backtrack(target,res,[])
        return res
