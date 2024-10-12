class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        currentsum = 0
        for i in gain:
            currentsum += i
            highest = max(highest,currentsum)
        return highest