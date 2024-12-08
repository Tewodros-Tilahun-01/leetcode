class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        dic = {}
        i = 0
        count = 0
        while i < len(arr):
            j = i + 1
            while j < len(arr):
                dic[ arr[i]/arr[j] ] = [ arr[i] ,arr[j] ]
                j += 1
            i += 1
        dic = dict(sorted(dic.items()))
        for i ,v in dic.items():
            count += 1
            if k == count:
                return v
        return []