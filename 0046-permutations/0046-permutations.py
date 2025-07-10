class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def perm(p,up):
            nonlocal res
            if not up:
                res.append(p)
                return
            num = up[0]
            for i in range(len(p)+1):
                perm(p[:i] + [num] + p[i:],up[1:])
        perm( [ nums[0] ], nums[1:] )
        return res
   