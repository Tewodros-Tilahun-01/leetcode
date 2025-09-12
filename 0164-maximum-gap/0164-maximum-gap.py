class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        def counting_sort(arr,exp):
            nonlocal n
            count = [0] * 10
            temp_res = [0] * n

            for i in range(n):
                digit = arr[i] // exp
                count[digit % 10] += 1
            
            for i in range(1,10):
                count[i] = count[i] + count[i-1]

            for i in range(n-1,-1,-1):
                digit = arr[i] // exp
                temp_res [ count[digit % 10 ] - 1 ] = arr[i]
                count[digit % 10] -= 1

            arr[:] = temp_res


        def redix_sort(arr):
            max_element = max(arr)
            exp = 1
            while max_element // exp:
                counting_sort(arr,exp)
                exp *= 10
            return arr

        redix_sort(nums)
        res = 0
        for i in range(1,n):
            res = max(res , nums[i]-nums[i-1])
        
        return res