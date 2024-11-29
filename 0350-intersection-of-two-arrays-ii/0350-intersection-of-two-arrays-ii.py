class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        nums1.sort()
        nums2.sort()
        pt1 , pt2 = 0,0
        while pt1 < len(nums1) and pt2 < len(nums2):
            i , j = nums1[pt1],nums2[pt2]
            if i == j:
                res.append(i)
                pt1 += 1
                pt2 += 1
            elif i > j:
                pt2 += 1
            else:
                pt1 += 1
        return res
            