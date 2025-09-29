class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        neg = 0
        small = float("inf")
        res = 0
        zero = False

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero = True 
                elif matrix[i][j] < 0:
                    neg += 1                
                    matrix[i][j] *= -1
                small = min(small,abs(matrix[i][j]))
                res += matrix[i][j]
                
        if neg % 2 == 1 and not zero:
            res -= (2 * small)
            
        return res