class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        hashmap = set()
        res = 1
        while j < len(s):
            letter = s[j]
            if letter in hashmap:
                hashmap.remove(s[i])
                i += 1
            else:
                hashmap.add(letter)
                j += 1
            res = max(res,j-i)
        return res
