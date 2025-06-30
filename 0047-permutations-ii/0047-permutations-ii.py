class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        
        def helper(p,up):
            if len(up) == 0:
                res.add(tuple(p))
                return
            val = up[0]
            for i in range(len(p)+1):
                helper( p[:i] + [ val ]+  p[i:],up[1:])
        helper([],nums)
        return list(res)