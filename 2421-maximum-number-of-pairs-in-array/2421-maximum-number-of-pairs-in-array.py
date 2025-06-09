class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        count = 0
        re= 0
        setList = defaultdict(int)
        for i in nums:
            setList[i] += 1
            re += 1
            if setList[i] % 2 == 0:
                count += 1
                re -= 2
        return[count,re]