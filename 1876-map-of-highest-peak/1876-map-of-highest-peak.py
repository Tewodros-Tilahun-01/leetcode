class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        queue = collections.deque()
        maxRow = len(isWater)
        maxCol = len(isWater[0])
        dir = [(0,1),(0,-1),(1,0),(-1,0)]
        def isValid(row,col):
            return 0 <= row < maxRow and 0 <= col < maxCol and isWater[row][col] != 0

        for i in range(maxRow):
            for j in range(maxCol):
                if isWater[i][j] == 0:
                    isWater[i][j] = float("inf")
                else:
                    isWater[i][j] = 0
                    queue.append((i,j))
        while queue:
            row , col = queue.popleft()
            current = isWater[row][col]
            for dx , dy in dir:
                new_row , new_col = row + dx , col + dy
                if 0 <= new_row < maxRow and 0 <= new_col < maxCol and isWater[new_row][new_col] != 0:
                    if isWater[new_row][new_col] > current + 1:
                        isWater[new_row][new_col] = current + 1
                        queue.append((new_row,new_col))
        return isWater


                