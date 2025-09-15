class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        count = 0
        for i in range(n):
            current_gcd = nums[i]
            for j in range(i, n):
                current_gcd = gcd(current_gcd, nums[j])
                if current_gcd == k:
                    count += 1
                elif current_gcd < k:
                    break
        return count