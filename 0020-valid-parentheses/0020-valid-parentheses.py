class Solution:
    def isValid(self, s: str) -> bool:
       check = { "(":")","{":"}","[":"]" }
       stack = []
       for op in s:
            if op in check:
                stack.append(op)
            else:
                if len(stack) == 0:return False
                else:
                    if check [stack.pop()] != op:
                        return False
       return True if len(stack) == 0 else False

        
        
