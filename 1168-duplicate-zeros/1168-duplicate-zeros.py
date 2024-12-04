class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        pt1 = 0
        n = len(arr)
        while pt1 < n-1:
            if arr[pt1] == 0:
                arr[:] = arr[:pt1 + 1] + [0] + arr[pt1 +1 :n-1] 
                pt1 += 1
            pt1 += 1      
