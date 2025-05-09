class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        s = sorted(nums)
        count = {}
        res = []
        for i in range(len(nums)):
            if s[i] not in count:
                count[s[i]] = i
        for i in nums:
            res.append( count[i] )
        return res