class Solution:
    def minimumSteps(self, s: str) -> int:
        white = 0
        counter = 0
        for i in range(len(s)):
            if s[i] == '0':
                counter = counter + i - white
                white += 1
        return counter