class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        return min(count["b"],count["a"],count["n"],count["l"]//2,count["o"]//2)
            