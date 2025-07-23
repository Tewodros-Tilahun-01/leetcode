class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        length = len(nums)
        if length <= 2:
            return True
        
        issues = 0
        idx = 0
        while idx < length - 1:
            if nums[idx] > nums[idx + 1]:
                if issues > 0:
                    return False
                issues += 1
                
                can_change_current = True
                if idx > 0 and nums[idx - 1] > nums[idx + 1]:
                    can_change_current = False
                
                can_change_next = True
                if idx + 2 < length and nums[idx] > nums[idx + 2]:
                    can_change_next = False
                
                if not can_change_current and not can_change_next:
                    return False
                
                idx += 1
            else:
                idx += 1
                
        return True