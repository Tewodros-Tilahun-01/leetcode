class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def perm(p,up,res): 
            if not up:
                res.append(p)
                return res
            num = up[0]
            for i in range(len(p)+1):
               perm(p[:i] + [num] + p[i:],up[1:],res)
            return res
        return perm( [ nums[0] ] , nums[1:] ,[] )
   