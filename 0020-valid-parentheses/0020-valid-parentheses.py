class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for op in s:
            if op in ["}","]",")"] and len(stack) == 0:
                return False
            if op in ["(" ,"{","["]:
                stack.append(op)
            elif op == "}":
                if stack.pop() != "{":
                    return False
            elif op == ")":
                if stack.pop() != "(":
                     return False
            elif op == "]":
                if stack.pop() != "[":
                     return False
        if len(stack) == 0:
            return True
        else:
            return False
        