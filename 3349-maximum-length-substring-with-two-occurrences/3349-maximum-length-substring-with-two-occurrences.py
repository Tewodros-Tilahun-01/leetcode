class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count  = defaultdict(int)
        left , right = 0 , 0
        res = 0
        while right < len(s):
            if count[s[right]] <= 2:
                count[ s[right] ] += 1

            while count[ s[right] ] == 3:
                count[ s[left] ] -= 1
                left += 1

            right += 1
            res = max(res,right - left)

        return res