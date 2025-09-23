class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        hashmap = set(nums)

        for n in hashmap:
            if (n-1) not in hashmap:
                i = 1
                while (n+i) in hashmap:i += 1
                res = max(res, i)
        
        return res