class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = {}
        maxNum = 0 
        res = 0
        for i in set(nums):
            m = nums.count(i)
            count[i]=m
            maxNum = max(m,maxNum)
            
        for i in count:
            if count[i] == maxNum:
                res +=count[i]
        return res