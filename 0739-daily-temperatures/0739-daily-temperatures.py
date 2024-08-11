class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = []
        for i in range(len(temperatures)-1,-1,-1):
            while len(stack) != 0 and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            if len(stack) == 0:
                ans.insert(0,0)
            else:
                ans.insert(0,stack[-1] - i)
            stack.append(i)
        return ans