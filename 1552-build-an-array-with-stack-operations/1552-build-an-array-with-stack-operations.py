class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        op = ["Push","Pop"]
        stack = []
        res = []
        ptr = 0
        for i in range(1,n + 1):
            stack.append(i)
            res.append(op[0])
            if stack[-1] != target[ptr]:
                stack.pop()
                res.append(op[1])
            else:
                ptr += 1
            if target == stack:
                return res 
        return []
