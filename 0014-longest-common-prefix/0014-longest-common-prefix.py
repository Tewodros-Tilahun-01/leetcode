class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        prefix = strs[0]
        for word in strs:
            for index in range(len( prefix )):
                if word[index] != prefix[index]:
                    prefix = prefix[:index]
                    break
        return prefix
