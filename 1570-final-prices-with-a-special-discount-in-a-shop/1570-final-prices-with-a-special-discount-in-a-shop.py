class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        res = [0] * len(prices)
        for i in range(len(prices)-1,-1,-1):
            while len(stack) and stack[-1] > prices[i]:
                stack.pop()
            if not len(stack):
                res[i] = prices[i]
            else:
                res[i] = prices[i] - stack[-1]
            stack.append(prices[i])
        return res