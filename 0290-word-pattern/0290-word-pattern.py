class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        if len((pattern)) != len((s)):
            return False
        dic = {}
        maped =[]
        for i in range(len(pattern)):
            if s[i] not in dic: 
                if pattern[i] not in maped:
                    dic[s[i]] = pattern[i]
                    maped.append(pattern[i])
                else:
                    return False
            else:
                if dic[s[i]] != pattern[i]:
                    return False
        return True            