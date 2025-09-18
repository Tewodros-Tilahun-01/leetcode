class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        dir = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
        rows , cols = len(img) , len(img[0])
        res = [[0]*cols for _ in range(rows)]
        
        def is_valid(row,col):
            return 0 <= row < rows and 0 <= col < cols

        for i in range(rows):
            for j in range(cols):
                total = img[i][j] 
                nums = 1
                for dx , dy in dir:
                    row ,col = i + dx , j + dy
                    if is_valid(row,col):
                        total += img[row][col]
                        nums += 1
                res[i][j] = total // nums
        
        return res
                   
