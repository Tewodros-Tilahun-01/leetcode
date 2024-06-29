class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        size = len(nums)/2
        count = defaultdict(int)
        for i in nums:
            count[i] = count[i]+1
        
        for key , value in count.items():
           
            if value > size:
                return key
                
