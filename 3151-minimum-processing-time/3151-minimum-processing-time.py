class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse = True)
        processorTime.sort()
        res = 0
        for j in range(len(processorTime)):
            index = 4 * j
            for i in range(index , index + 4):
                res = max(res,tasks[i] + processorTime[j])
        return res