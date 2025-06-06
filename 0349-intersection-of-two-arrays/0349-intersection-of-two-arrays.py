class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        set1 = set(nums2)
        for i in nums1:
            if i in set1:
                res.add(i)
        return list(res)