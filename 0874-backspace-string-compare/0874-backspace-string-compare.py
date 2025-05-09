class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def check(word):
            stack = []
            for i in word:
                if i == "#" and len(stack) != 0:
                    stack.pop()
                elif i != "#":
                    stack.append(i)
            return stack
        return check(s) == check(t)

            