class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        average = []
        for i in range(len(nums)//2):
            maxPrt = len(nums)-i-1
            av = (nums[i] + nums[maxPrt])/2
            average.append(av)
        return min(average)
        