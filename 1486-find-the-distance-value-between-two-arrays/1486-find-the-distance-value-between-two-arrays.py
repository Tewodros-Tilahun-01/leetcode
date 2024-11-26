class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        count = 0
        for i in arr1:   
            right = len(arr2)-1
            left = 0
            while left <= right:
                mid =(left + right) // 2
                target = abs(i-arr2[mid])
                if target <= d:
                    count += 1
                    break
                if i < arr2[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return len(arr1)-count

                