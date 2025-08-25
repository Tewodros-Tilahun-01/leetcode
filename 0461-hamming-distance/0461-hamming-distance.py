class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        one = 1
        distance = 0
        while x  or  y:
            if x & 1 != y & 1:
                distance += 1
            x , y = x >>1 , y >>1

        return distance
        