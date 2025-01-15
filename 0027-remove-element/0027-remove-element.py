class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for j in nums:
            if j != val: 
                nums[count] = j
                count = count +1
        return count

