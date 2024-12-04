class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        pt = 0
        res = []
        while pt < len(nums):
            a = nums[pt]
            b = ""
            while pt < len(nums)-1 and nums[pt+1] == nums[pt] + 1:
                    b = "->" + str(nums[pt+1])
                    pt +=1
            res.append(str(a)+b)
            pt += 1
        return res