class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        count_num = 2000
        for i in "balon":
            if i not in count:
                return 0
            else:
                if i in ["l","o"]:
                    count[i] = count[i] // 2
                count_num = min(count_num,count[i])
        return count_num
            