class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # O(N)
        nums = list(set(nums))
        
        maxim = nums.pop(nums.index(max(nums)))
        if len(nums) < 2: # bcs already popped first max
            return maxim
        
        for iteration in range(2):
            maxim = nums.pop(nums.index(max(nums)))
        return maxim