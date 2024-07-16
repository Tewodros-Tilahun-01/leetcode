class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        sorted_nums = sorted(set(nums))
        count = 1
        max_num = 1
        # print(sorted_nums)
        for i in range(len(sorted_nums)):
            # if the list is in the last number break
            if i == len(sorted_nums)-1:
                break 
            if(sorted_nums[i] + 1 == sorted_nums[i+1]):
                max_num += 1  
                if max_num >  count:
                    count = max_num
            else:
                max_num = 1    
            
        return count