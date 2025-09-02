class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        max_num = nums[-1]
        op = 0
        for i in  range(n-2,-1,-1):
            current_num = nums[i]
            if current_num < max_num:
                max_num = current_num
                continue
            parts = math.ceil(nums[i] / max_num)
            op += parts - 1
            max_num = nums[i] // parts
        return op

