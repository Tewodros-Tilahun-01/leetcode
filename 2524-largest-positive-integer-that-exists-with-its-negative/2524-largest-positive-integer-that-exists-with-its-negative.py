class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        count = set()
        maxNum = -1
        for i in nums:
            if -i in count:
                maxNum = max(maxNum, i )
                maxNum = max(maxNum, -i )
            else:
                count.add(i)

        return maxNum