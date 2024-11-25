class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums)-2):
            target = 0 - nums[i]
            j = i + 1
            k = len(nums) - 1 
            while j < k:
                temp = nums[j] + nums[k]
                if target == temp:
                    l = ( nums[i] , nums[j],nums[k] )
                    if l not in res:res.add(l)
                    j += 1
                    k -= 1
                elif target < temp:
                    k -= 1
                else:
                    j += 1
        return list(res)