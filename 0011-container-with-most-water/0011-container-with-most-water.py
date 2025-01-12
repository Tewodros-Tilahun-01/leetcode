class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        stptr = 0
        endptr = len(height)-1
        width = endptr
        while stptr < endptr:
            area = min(height[ stptr],height[endptr]) * width
            res = max(res , area)
            if height[stptr] < height[endptr]:
                stptr += 1
            else:
                endptr -= 1
            width -= 1
        return res