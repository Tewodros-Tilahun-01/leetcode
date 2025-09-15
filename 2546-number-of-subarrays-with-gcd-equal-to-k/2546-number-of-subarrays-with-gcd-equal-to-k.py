class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        count = 0
        for i in range(n):
            if nums[i] % k != 0:  # Skip if nums[i] is not divisible by k
                continue
            current_gcd = nums[i]
            for j in range(i, n):
                if nums[j] % k != 0:  # Skip if nums[j] is not divisible by k
                    break
                current_gcd = gcd(current_gcd, nums[j])
                if current_gcd < k:  # GCD cannot increase, so break
                    break
                if current_gcd == k:
                    count += 1

        return count