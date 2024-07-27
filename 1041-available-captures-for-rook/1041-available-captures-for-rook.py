class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
       

        count = 0
        x=0
        y=0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "R":
                  x = i
                  y = j
        for i in range(x,-1,-1):
            if board[i][y] == "B":
                break
            if board[i][y] == "p":
                count +=1
                break
        for i in range(x,len(board)):
            if board[i][y] == "B":
                break
            if board[i][y] == "p":
                count += 1
                break
            
        for i in range(y,-1,-1):
            if board[x][i] =="B" :
                break
            if board[x][i] == "p":
                count += 1
                break
        for i in range(y,len(board[x])):
            if board[x][i] == "B":
                break
            if board[x][i] == "p":
                count += 1
                break
        return count