class Solution:
    def canCompleteCircuit(self,gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
            
        current = 0
        start = 0
        
        for i in range(len(gas)):
            current += gas[i] - cost[i]
            
            if current < 0:
                start = i + 1
                current = 0
        if start < len(gas):
            return start 
        return  -1