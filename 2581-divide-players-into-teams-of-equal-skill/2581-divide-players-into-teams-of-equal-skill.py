class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)//2
        res = 0
        paris = [(i,j) for i,j in zip( skill[:n] , skill[:n-1:-1] ) ]
        size = paris[0][0] + paris[0][1]
        for i , j in paris:
            if(i+j != size):
                return -1
            res += i*j
        return res