class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:


        def merge_sort(left:int,right:int,array:list) -> list: 
            if left == right:
                return [array[left]]
            mid = left + (right - left) // 2
            left = merge_sort(left,mid,array)
            right = merge_sort(mid+1,right,array)
            return merge(left,right)

        def merge(left:list,right:list)->list:
            i = j = 0
            sorted_array = []
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    sorted_array.append(left[i])
                    i += 1
                else:
                    sorted_array.append(right[j])
                    j += 1
            sorted_array.extend(left[i:])
            sorted_array.extend(right[j:])
            
            return sorted_array

        return merge_sort(0,len(nums)-1,nums)
        
        

            
