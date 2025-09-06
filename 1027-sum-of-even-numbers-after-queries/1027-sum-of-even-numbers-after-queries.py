class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = sum(num for num in nums if num % 2 == 0)
        result = []
        
        for val, idx in queries:
            old_val = nums[idx]
            nums[idx] += val
            new_val = nums[idx]
            
            if old_val % 2 == 0:
                even_sum += val if new_val % 2 == 0 else -old_val
            elif new_val % 2 == 0:
                even_sum += new_val
                
            result.append(even_sum)
        
        return result