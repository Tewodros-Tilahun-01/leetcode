class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(start: int, end: int, arr: List[int]) -> None:
            if start >= end:
                return
            
            mid = start + (end - start) // 2
            merge_sort(start, mid, arr)
            merge_sort(mid + 1, end, arr)
            merge(start, mid, end, arr)
        
        def merge(start: int, mid: int, end: int, arr: List[int]) -> None:
            # Create temporary array for merging
            temp = arr[start:end + 1]
            left, right = 0, mid - start + 1
            i = start
            
            # Merge two sorted subarrays
            while left <= mid - start and right <= end - start:
                if temp[left] <= temp[right]:
                    arr[i] = temp[left]
                    left += 1
                else:
                    arr[i] = temp[right]
                    right += 1
                i += 1
            
            # Copy remaining elements from left subarray
            while left <= mid - start:
                arr[i] = temp[left]
                left += 1
                i += 1
                
        merge_sort(0, len(nums) - 1, nums)
        return nums