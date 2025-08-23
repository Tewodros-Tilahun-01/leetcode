class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        hashmap = {}
        n = len(s)
        res = [0] * n
        for i in range(n):
            hashmap[indices[i]] = s[i]

        for i in range(n):
            res[i] = hashmap[i]
        return "".join(res)