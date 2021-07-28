class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Find Pivot in nums with Binary Search
        # Merge sort
        # return squares
        
        # find pivot:
        
        length = len(nums)
        
        if len(nums) == 1:
            positive_ind = 0
        else:
            positive_ind = -1
        
        for i in range(length):
            if nums[i] >= 0:
                positive_ind = i
                break
            
        
        nums_neg = nums[:positive_ind][::-1]
        nums_pos = nums[positive_ind:]
        
        # merge sort and square:
        i = j = k =  0
        while i < len(nums_neg) and j < len(nums_pos):
            if (-nums_neg[i]) < nums_pos[j]:
                nums[k] = nums_neg[i]**2
                i += 1
            else:
                nums[k] = nums_pos[j]**2
                j += 1
            k += 1
        
        # Checking if any element was left
        while i < len(nums_neg):
            nums[k] = nums_neg[i]**2
            i += 1
            k += 1
            
        while j < len(nums_pos):
            nums[k] = nums_pos[j]**2
            j += 1
            k += 1
        
        return(nums)
            