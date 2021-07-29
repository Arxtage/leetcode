class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # O(n)
        tmp = None
        for i in reversed(range(len(nums) - 1)):

            i = len(nums) - 2

            while i >= 0:
                if nums[i] < nums[i+1]:
                    # значимо
                    nums[i+1:] = sorted(nums[i+1:])
                    for j in range(i+1, len(nums)):
                        if nums[j] > nums[i]:
                            tmp = nums[i]
                            nums[i] = nums[j]
                            nums[j] = tmp
                            return(nums)
                i -= 1
            
        return(nums.sort())