class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:return False
        asc = True
        first = len(arr)
        for i in range(1,len(arr)):
            if arr[i-1] > arr[i]:
                asc = False
                first = min(i-1,first)
            if arr[i-1] >= arr[i] and asc:return False
            if arr[i-1] <= arr[i] and not asc:return False

        return True and not asc and first != 0
            
                
                    


