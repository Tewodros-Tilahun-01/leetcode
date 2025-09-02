class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        
        coins.sort()

        max_reach = 0  
        for coin in coins:
            if coin > max_reach + 1:
                break
            max_reach += coin
        return max_reach + 1
            
            

            
