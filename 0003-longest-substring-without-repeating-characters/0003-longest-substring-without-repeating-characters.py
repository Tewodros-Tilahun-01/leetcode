class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        longest = 0
        visited = set()
        while j < len(s):
            if s[j] in visited:
                visited.remove(s[i])
                i += 1
            else:
                visited.add(s[j])
                j += 1
            longest = max(longest,j-i)
        return longest
