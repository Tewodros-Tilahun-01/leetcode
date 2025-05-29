class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        count = Counter(nums2)
        for i in nums1:
            if count[i] >= 1:
                res.append(i)
                count[i] -= 1 
        return res