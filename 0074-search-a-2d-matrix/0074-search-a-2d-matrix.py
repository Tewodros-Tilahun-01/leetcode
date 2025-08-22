class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row,col = len(matrix)-1 , len(matrix[0])-1
        left = [0,0]
        right = [row,col]
        mid = [0] * 2
        while (left[1] <= right[1] and left[0] == right[0] ) or  left[0] < right[0]:
            l = left[0] * (col+1)  + left[1]
            r = right[0] * (col+1) + right[1]
            m = (l + r) // 2
            mid[0],mid[1] = m//(col+1) , m % (col+1)
            if target == matrix[mid[0]][mid[1]]:
                return True
            elif target < matrix[mid[0]][mid[1]]:
                if mid[1] == 0:
                    right[0] = mid[0] - 1
                    right[1] = col
                else:
                    right[0] = mid[0]
                    right[1] = mid[1] - 1
            else:
                if mid[1] == col:
                    left[0] = mid[0] + 1
                    left[1] = 0
                else:
                    left[0] = mid[0] 
                    left[1] = mid[1] + 1
        return False
