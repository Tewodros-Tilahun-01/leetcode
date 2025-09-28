class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        left = right = 0
        for num in nums:
            if num == 1:
                right += 1
        max_score = right + left
        res = [0]

        for i in range(len(nums)):
            if nums[i] == 0:
                left += 1
            else:
                right -= 1
            cur_score = right + left
            if cur_score > max_score:
                max_score = cur_score
                res = [i+1]
            elif cur_score == max_score:
                res.append(i+1)
        
        return res


