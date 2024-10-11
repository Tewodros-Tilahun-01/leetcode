class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minDiff = 100
        runSum = 0
        for i in nums:
            runSum += i
            minDiff = min(minDiff,runSum)
        if minDiff <= 0:
            return minDiff * -1 +1
        return 1