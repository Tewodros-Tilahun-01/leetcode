class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])-1

        for row in range(rows):
            left , right = 0 , cols
            while left <= right:
                if image[row][left] == image[row][right]:
                    image[row][left] = image[row][right] = int(not bool(image[row][left]))
                left , right = left+1 , right-1
        
        return image
