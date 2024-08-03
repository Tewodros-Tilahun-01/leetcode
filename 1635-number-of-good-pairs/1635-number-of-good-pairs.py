class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        count  = defaultdict(int)
        if len(nums) == len(set(nums)):
            return 0
        for i in nums:
            count[i] += 1
        for key in count:
            num = count[key]
            if num > 1:                
                res +=int(((num-1)*num)/2)
        return res
