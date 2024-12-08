class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        target = 2 * sum(skill) // len(skill)        
        chemistry = 0     
        cnt = Counter(skill)                 

        for v, c in cnt.items():           
            if c != cnt[target - v]:             
                return -1                 
            chemistry += c * v * (target - v)    
            
        return chemistry // 2 