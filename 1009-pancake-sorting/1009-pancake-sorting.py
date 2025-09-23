class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def filp(right,arr):
            left = 0
            while left <= right:
                arr[left] , arr[right] =  arr[right] , arr[left]
                left += 1
                right -= 1


        last = len(arr)-1
        first = 0
        res = []
        while last > 0:
            if last + 1 == arr[last] :
                last -= 1
                continue
            if arr[0] == last + 1:
                filp(last,arr)
                res.append(last+1)
            elif arr[first] == last + 1:
                filp(first,arr)
                res.append(first+1)
                first = 0
            else:
                first += 1

        return res
                
