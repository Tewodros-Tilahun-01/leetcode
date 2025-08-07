class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        index = 0
        check = set()
        for i in nums:
            if i not in check:
                nums[index] = i
                check.add(i)
                index += 1
                k += 1
        return k
        