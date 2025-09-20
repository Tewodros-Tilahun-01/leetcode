class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        visited = [False] + [True] * n
        count = n
        def cycle(i,j):
            nonlocal visited , n , k , count
            if count == 1:
                return 
            if j == k:
                visited[i] = False
                count -= 1
                j = 0
            i = (i + 1) % (n+1)
            while not visited[i]:
                i = (i + 1) % (n+1)
            cycle(i,j+1)
        cycle(0,0)
        for i in range(n+1):
            if visited[i]:
                return i

            

            
            