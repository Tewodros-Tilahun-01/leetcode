class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        major = len(nums)//3
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1
            if hashmap[num] == major+1:
                res.append(num)
        return res
