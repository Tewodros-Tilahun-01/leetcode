class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        res = 0
        answered = {}
        for i in answers:
            if i not in answered or i == 0:
                res += 1 + i
                answered[i] = i
            elif answered[i] > 0:
                answered[i] -= 1 
            else:
                answered[i] = i 
                res += 1 + i
        return res