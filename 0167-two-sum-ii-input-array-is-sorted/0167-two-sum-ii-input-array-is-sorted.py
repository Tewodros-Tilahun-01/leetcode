class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i , j = 0 , len(numbers)-1
        while i < j:
            _sum = numbers[i] + numbers[j] 
            if _sum == target:
                return [i+1,j+1]
            elif _sum < target:
                i += 1
            else:
                j -= 1
        