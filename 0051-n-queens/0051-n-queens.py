class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        dir = [(-1,0),(-1,-1),(-1,1)]
        board = [["."] * n for _ in range(n)]
        
        def is_valid(row,col,board):
            for dx ,dy in dir:
                new_row , new_col = row + dx , col + dy
                while 0 <= new_row < n and 0 <= new_col < n:
                    if board[new_row][new_col] == "Q":
                        return False
                    new_row , new_col = new_row + dx , new_col + dy
            return True
        
        def backtrack(row,board):
            nonlocal res
            if row == n:
                res.append(["".join(row) for row in board])
                return
            
            for col in range(n):
                if is_valid(row,col,board):
                    board[row][col] = "Q"
                    backtrack(row+1,board)
                    board[row][col] = "."
        
        res = []
        backtrack(0,board)
        return res


