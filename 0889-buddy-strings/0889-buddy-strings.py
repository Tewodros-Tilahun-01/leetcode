class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):return False
        if len(set(s)) < len(s) and s == goal:return True
        count = 0
        set1 = set()
        set2 = set() 
        for i in range(len(s)):
            if s[i] != goal[i]:
                count += 1
                set1.add(s[i])
                set2.add(goal[i])
        if count == 2 and set1 == set2 :
            return True
        else:
            return False