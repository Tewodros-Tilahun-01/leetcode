class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dir = [(0,1),(1,0),(-1,0),(0,-1)]
      
        def dfs(row,col):
            if board[row][col] != "O":
                return 
            # make "N" for those cell that are connected to the edge
            board[row][col] = "N"
            for x , y in dir:
                new_row = row + x 
                new_col = col + y
                if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]):
                    dfs(new_row,new_col)
        i = 0
        j = 0
        rev = True

        # check the edges if we get "O" then call dfs on those cells 
        while (not (i == 0 and j == 0)) or  rev:
            dfs(i,j)
            if i < len(board)-1 and rev:
                i += 1
            elif j < len(board[0])-1 and rev:
                j += 1 
            elif i > 0 :
                i -= 1 
                rev = False
            elif j > 0:
                j -= 1
            else:
                break

        # make the "N" to "O" and other to "X"
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "N":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"
            
        
        
            
            
        