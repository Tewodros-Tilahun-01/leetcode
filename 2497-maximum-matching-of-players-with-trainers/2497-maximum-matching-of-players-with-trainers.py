class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        count = i = j = 0
        players.sort()
        trainers.sort()
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                count += 1
                i , j = i+1 , j+1
            else:j += 1
        return count