class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        high = []
        equal = []
        for i in nums:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                high.append(i)
            else:
                equal.append(i)
        return less + equal + high