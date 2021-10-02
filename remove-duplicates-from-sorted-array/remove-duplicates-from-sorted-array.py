class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #O(n)
        
        res = 0
        
        i = 0
        k = 0
        while i < len(nums):
            nums[k] = nums[i]
            cur = nums[i]
            i+=1
            while i < len(nums) and nums[i] == cur:
                i+=1
            res += 1
            k += 1
        return res