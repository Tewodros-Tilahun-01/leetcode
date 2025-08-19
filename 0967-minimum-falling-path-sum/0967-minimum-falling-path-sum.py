class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        
        # Process from second-to-last row upwards
        for i in range(n-2, -1, -1):
            for j in range(n):
                # Get minimum from three possible directions
                min_path = matrix[i+1][j]  # Straight down
                if j > 0:  # Check left diagonal
                    min_path = min(min_path, matrix[i+1][j-1])
                if j < n-1:  # Check right diagonal
                    min_path = min(min_path, matrix[i+1][j+1])
                matrix[i][j] += min_path
        
        return min(matrix[0])