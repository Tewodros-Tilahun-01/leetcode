class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        count = 0
        set1 = set()
        set2 = set() 
        set3 = set()
        for i in range(len(s)):
            if s[i] != goal[i]:
                count += 1
                set1.add(s[i])
                set2.add(goal[i])
            else:
                set3.add(s[i])
        print(set1 == set2)
        if count == 2 and set1 == set2 or count == 0 and len(set3) <= len(s) -1:
            return True
        else:
            return False