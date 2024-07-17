class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_number = max(candies)
        res = []
        for i in candies:
            if (max_number <= i + extraCandies):
                res.append(True)
            else:
                res.append(False)
        return res