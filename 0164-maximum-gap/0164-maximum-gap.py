class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
            
        def counting_sort(arr, exp):
            n = len(arr)
            count = [0] * 10
            output = [0] * n
            
            for num in arr:
                digit = (num // exp) % 10
                count[digit] += 1
            
            for i in range(1, 10):
                count[i] += count[i-1]
            

            for num in arr[::-1]:
                digit = (num // exp) % 10
                count[digit] -= 1
                output[count[digit]] = num
            

            arr[:] = output
        
        def radix_sort(arr):
            max_num = max(arr)
            exp = 1
            while max_num // exp:
                counting_sort(arr, exp)
                exp *= 10
        
        radix_sort(nums)
        
        
        res = 0
        for i in range(1, len(nums)):
            res = max(res, nums[i] - nums[i-1])
        
        return res