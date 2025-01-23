class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = 1
        res = 0
        temp = 0
        while right < len(height):
            if height[left] > height[right]:
                temp += height[left] - height[right]
            else:
                res += temp
                temp = 0
                left = right
            right += 1
        right = len(height)-1
        left = right - 1
        temp = 0
        while left >= 0:
            if height[right] > height[left]:
                temp += height[right] - height[left]
            elif height[right] == height[left]:
                print("pass this one")
            else:
                res += temp
                temp = 0
                right = left
            left -= 1 
       
        return res

