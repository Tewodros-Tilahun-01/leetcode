class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        num = set(arr)
        if arr.count(0) > 1:
            return True
        for i in arr:
            if i * 2 in num and i != 0:
                return True
        return False
