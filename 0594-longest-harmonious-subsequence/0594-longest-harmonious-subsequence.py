class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        max_length = 0
        
        # Check each number in the frequency counter
        for num in count:
            # If num + 1 exists in the counter
            if num + 1 in count:
                # Calculate length of subsequence with num and num + 1
                current_length = count[num] + count[num + 1]
                max_length = max(max_length, current_length)
        
        return max_length