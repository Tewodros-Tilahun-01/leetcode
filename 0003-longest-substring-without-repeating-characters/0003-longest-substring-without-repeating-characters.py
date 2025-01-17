class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = set()
        left = 0
        right = 0
        res = 0
        while right != len(s):
            if s[right] not in sub:
                res = max(res,right-left + 1)
                sub.add(s[right])
                right += 1     
            else:
                while s[right] in sub:
                    sub.remove(s[left])
                    left += 1 
        return res