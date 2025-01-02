class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        for i in range(len(prices)-1,-1,-1):
            while len(stack) and stack[-1] > prices[i]:
                stack.pop()
            temp = prices[i]
            if stack :
               prices[i] = prices[i] - stack[-1]
            stack.append(temp)
        return prices