class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_number = 0
        res = []
        for num in candies:
            max_number = max(max_number,num)
        for i in candies:
            if (max_number <= i + extraCandies):
                res.append(True)
            else:
                res.append(False)
        return res