class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visted = set()
        dir = [[0,1],[0,-1],[1,0],[-1,0]]
        
        def backtrack(board,index,row,col):
            if index == len(word):
                return True

            flag = False
            for r , c in dir:
                nx = r + row 
                ny = c + col
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]) \
                and word[index] == board[nx][ny] and (nx,ny) not in visted:
                    visted.add((nx,ny)) 
                    if backtrack(board,index+1,nx,ny):
                        flag = True
                    visted.remove((nx,ny))
            return flag
            

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] :
                    visted.add((i,j))
                    if backtrack(board,1,i,j):
                        return True
                    visted.remove((i,j))
        return False

                   
                

                 