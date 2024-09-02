class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        l_sum = []
        r_sum = []
        sum = 0
        for i in nums:
            l_sum.append(sum)
            sum += i
        sum = 0
        for i in range(0,len(nums)):
            r_sum.insert(0,sum)
            sum += nums[-1-i]
        ans = []
        for i in range(0,len(nums)):
            ans.append( abs( l_sum[i] - r_sum[i] ))
        return ans