class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        pre = [0] * n
        suf = [0] * n

        pre[0] = nums[0]
        suf[n - 1] = nums[n - 1]

        for i in range(1, n):
            pre[i] = pre[i - 1] + nums[i]
            suf[n - i - 1] = suf[n - i] + nums[n - i - 1]

        for i in range(n):
            left = nums[i] * i - pre[i]
            right = suf[i] - nums[i] * (n - i - 1)
            res[i] = left + right

        return res
