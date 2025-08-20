class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        playerDistance = abs(target[0] - 0)+ abs(target[1] - 0)

        for ghost in ghosts:
            ghostDistance = abs(target[0] - ghost[0])+ abs(target[1] - ghost[1])
            if ghostDistance <= playerDistance:
                return False
        return True