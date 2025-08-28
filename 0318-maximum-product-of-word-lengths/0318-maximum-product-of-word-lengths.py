class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        bit_vector = [0] * n
        res = 0
        for i in range(n):
            for c in words[i]:
                bit_vector[i] |= (1 << (ord(c) - ord('a')))
        for i in range(n):
            for j in range(i+1):
                if (bit_vector[i] & bit_vector[j]) == 0:
                    res = max(res,len(words[i]) * len(words[j]))
        return res