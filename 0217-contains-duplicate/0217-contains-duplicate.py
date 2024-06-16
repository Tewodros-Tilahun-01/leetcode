class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        setnums = set(nums)
        return False if( len(nums) == len(setnums)) else True
        