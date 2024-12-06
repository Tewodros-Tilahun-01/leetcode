class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = []
        less = []
        more = []
        for i in nums:
            if i < 0:
                less.append(i)
            else:
                more.append(i)
        i = 0
        while i < len(nums)/2:
            res.append(more[i])
            res.append(less[i])
            i += 1
        return res

            
        

        