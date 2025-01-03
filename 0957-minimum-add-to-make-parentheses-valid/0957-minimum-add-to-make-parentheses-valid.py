class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        temp = 0
        for i in s:
            if i == "(":
                stack.append("(")
            elif stack:
                stack.pop()
            else:
                temp += 1
        return len(stack) + temp
