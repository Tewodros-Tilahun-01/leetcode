class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxnum = float("-inf")
        sumNum = 0
        if len(nums) == k:
            return sum(nums)/k
        for i in range(len(nums)):
            if i < k:
                sumNum += nums[i]
            else:
                maxnum = max(sumNum/k,maxnum)
                sumNum -= nums[ i-k ] 
                sumNum += nums[ i ]
                maxnum = max(sumNum/k,maxnum)
        return maxnum