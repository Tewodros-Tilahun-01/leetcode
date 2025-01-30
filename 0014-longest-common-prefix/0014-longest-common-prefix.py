class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = [i for i in strs[0]]
        for i in strs:
            j = -1
            for j in range( min( len( i ) , len(word)  ) ):
                if word[j] != i[j]:
                    j -= 1
                    break
            word = word[:j+1]
        return "".join( word )