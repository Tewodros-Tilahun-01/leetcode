class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opr = set(["+","-","/","*"])
        stack = []
        def solve(y,x,opr):
            if opr == "+":return x + y
            if opr == "-":return x - y
            if opr == "/" and x * y > 0 :return math.floor(x / y)
            if opr == "/" and x * y < 0:return math.ceil(x / y)
            else:return x * y
        

        for i in tokens:
            if i in opr:
                var = solve(stack.pop(),stack.pop(),i)
                stack.append( var )
            else:
                stack.append(int(i))
        return stack[0]