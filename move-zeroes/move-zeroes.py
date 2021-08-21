class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Not optimal O(N) O(1)
        
        length = len(nums)
        
        # ind_insert = 0
        ind = 0
        
        while ind < length:
            if nums[ind] != 0:
                nums.append(nums[ind])
            ind += 1
         
        del nums[:length]
        
        while len(nums) < length:
            nums.append(0)
            