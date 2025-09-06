class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_value = 0
        res = []
        for num in nums:
            if num % 2 == 0:
                even_value += num
        
        for val, index in queries:
            if nums[index] % 2 == 0:
                even_value -= nums[index]

            nums[index] = nums[index] + val 
            if nums[index] % 2 == 0:
                even_value += nums[index]
                
            res.append(even_value)

        return res
