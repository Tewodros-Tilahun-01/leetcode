class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                nums3.append(nums2[j])
                j += 1
            else:
                nums3.append(nums1[i])
                i += 1

        while i < len(nums1):
            nums3.append(nums1[i])
            i += 1
        while j < len(nums2):
            nums3.append(nums2[j])
            j += 1

        n = len(nums3)
        print(nums3)
        if n % 2 == 0:
            return ( nums3[n//2] + nums3[n//2 - 1] ) / 2
        else:
            return nums3[n//2]