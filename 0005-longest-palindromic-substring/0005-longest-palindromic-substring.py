class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        resleft = resright = 0
        max_length = 0

        def explore(left,right):
            nonlocal resleft, resright, max_length
            while left >= 0 and right < n and s[left] == s[right]:
                curr_length = right - left + 1
                if curr_length > max_length:
                    max_length = curr_length
                    resleft = left
                    resright = right

                left , right = left - 1 , right + 1

        for i in range(0,n-1):
            left = right = i
            explore(left,right)
            explore(left,right + 1) 

        return s[resleft:resright+1]
            