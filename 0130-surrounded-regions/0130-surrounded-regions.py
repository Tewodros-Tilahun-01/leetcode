class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Modifies the board in-place to flip surrounded 'O' regions to 'X'.
        'O' regions connected to the border remain 'O'.
        """

        rows, cols = len(board), len(board[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  

        def dfs(row: int, col: int) -> None:
            """Marks 'O' cells connected to the border as 'N' using DFS."""
            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != "O":
                return
            board[row][col] = "N"  # Mark as connected to border
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                dfs(new_row, new_col)

        # Step 1: Traverse borders to find 'O' cells and mark connected regions
        row, col = 0, 0
        reverse = True  
        while (row != 0 or col != 0) or reverse:
            if board[row][col] == "O":
                dfs(row, col)
            # Move along borders: top -> right -> bottom -> left
            if row < rows - 1 and reverse:
                row += 1  
            elif col < cols - 1 and reverse:
                col += 1 
            elif row > 0:
                row -= 1  
                reverse = False
            elif col > 0:
                col -= 1  
            else:
                break

        # Step 2: Flip 'O' to 'X' (surrounded) and 'N' back to 'O' (not surrounded)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "N":
                    board[i][j] = "O"  
                else:
                    board[i][j] = "X"  
        