class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # O(n)
        res = 0
        maxim = nums[0]
        for i in range(len(nums) - 1):
            if nums[i+1]<= maxim:
                
                res += maxim + 1 - nums[i+1]
                maxim += 1
            else:
                maxim = nums[i+1]
        return res