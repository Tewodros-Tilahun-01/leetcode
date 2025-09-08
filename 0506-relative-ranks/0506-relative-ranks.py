class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        res = [0] * n

        hashmap = {}
        for i in range(n):
            hashmap[score[i] ] = i
            
        score.sort(reverse=True)

        for i in range(n):
            rank = ""
            if i == 0:
                rank = "Gold Medal"
            elif i == 1:
                rank = "Silver Medal"
            elif i == 2:
                rank = "Bronze Medal"
            else:
                rank = str(i+1)
            res[hashmap[score[i]]] = rank

        return res