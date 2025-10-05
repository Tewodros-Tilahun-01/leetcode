class Solution:
    def decodeString(self, s: str) -> str:
        
        def rec(num, path, index):
            if index >= len(s):
                return path
            
            char = s[index]
            if char.isdigit():
                return rec(num * 10 + int(char), path, index + 1)
            elif char == '[':
                substring, new_index = rec(0, "", index + 1)
                return rec(0, path + num * substring, new_index)
            elif char == ']':
                return path, index + 1
            else:
                return rec(num, path + char, index + 1)

        return rec(0, "", 0)