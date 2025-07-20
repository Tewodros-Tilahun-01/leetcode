class Solution:
    def maxArea(self, height: List[int]) -> int:
        ptr1 = max_capacity = 0
        ptr2 = width = len(height) - 1
         
        while ptr2 > ptr1:
            capacity = min(height[ptr1],height[ptr2]) * width
            max_capacity = max(max_capacity , capacity)
            if height[ptr1] < height[ptr2]:
                ptr1 += 1
            else:
                ptr2 -= 1
            width -= 1

        return max_capacity
