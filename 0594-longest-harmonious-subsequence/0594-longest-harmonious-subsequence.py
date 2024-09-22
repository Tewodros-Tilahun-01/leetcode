class Solution:
    def findLHS(self, nums: List[int]) -> int:
        coll = Counter(nums)
        maxnumber = 0
        for i in set(nums):
            if i-1 in coll:
                maxnumber = max(maxnumber,coll[i] + coll[i-1])
        return maxnumber