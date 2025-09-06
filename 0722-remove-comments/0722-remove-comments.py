class Solution:
    def removeComments(self,source):
        result = []
        current_line = []
        comment = False
        
        for line in source:
            i = 0
            if not comment:
                current_line = []
            
            while i < len(line):
                if comment:
                    if i + 1 < len(line) and line[i] == '*' and line[i + 1] == '/':
                        comment = False
                        i += 2
                    else:
                        i += 1
                else:
                    if i + 1 < len(line) and line[i] == '/' and line[i + 1] == '*':
                        comment = True
                        i += 2
                    elif i + 1 < len(line) and line[i] == '/' and line[i + 1] == '/':
                        break
                    else:
                        current_line.append(line[i])
                        i += 1
            
            if not comment and current_line:
                result.append(''.join(current_line))
        
        return result