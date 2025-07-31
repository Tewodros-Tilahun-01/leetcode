class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        p, n = 0, 1
        
        for i in nums:
            if i > 0:
                res[p] = i
                p += 2
        for i in nums:
            if i < 0:
                res[n] = i
                n += 2
        return res        

            
        

        