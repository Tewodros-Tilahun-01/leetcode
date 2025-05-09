class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0
            
        left = 0
        right = len(height) - 1
        left_max = right_max = water = 0
        
        while left < right:
            # Update the maximum height seen from left and right
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            
            # Water at current position is determined by the smaller of left_max and right_max
            if left_max <= right_max:
                water += left_max - height[left]
                left += 1
            else:
                water += right_max - height[right]
                right -= 1
                
        return water