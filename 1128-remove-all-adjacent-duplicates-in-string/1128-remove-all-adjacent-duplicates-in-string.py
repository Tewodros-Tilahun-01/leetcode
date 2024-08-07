class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if len(stack):
                prv = stack.pop()
                if prv != char:
                    stack.append(prv)
                    stack.append(char)
            else:
                stack.append(char)
        return "".join(stack)