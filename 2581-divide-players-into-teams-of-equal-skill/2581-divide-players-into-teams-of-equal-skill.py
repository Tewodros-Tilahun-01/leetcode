class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i , j = 0 , len(skill)-1
        chem = skill[i] * skill[j]
        total_skill = skill[i] + skill[j]
        i , j = i+1 , j-1

        while i < j:
            print(total_skill , skill[i] + skill[j])
            if total_skill != skill[i] + skill[j]:
                return -1
            else:
                chem += skill[i] * skill[j]
            i , j = i+1 , j-1
        
        return chem


