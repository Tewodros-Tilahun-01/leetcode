class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        nums2.sort()
        for i in nums1:
            right = len(nums2)-1
            left = 0
            while right >= left:
                mid = (right + left )//2
                if i == nums2[mid]:
                    res.append(i)
                    nums2.remove(i)
                    break
                elif i < nums2[mid]:
                    right = mid - 1              
                elif i > nums2[mid]:
                    left  = mid + 1
        return res
            