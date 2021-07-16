class Solution:
    def rob(self, nums: List[int]) -> int:
        # DP o(n)
        
        if len(nums) == 1:
            return(nums[0])
        DP = [0]*len(nums)
        DP[0] = nums[0]
        DP[1] = max(nums[0:2])
        for i in range(2,len(nums)):
            DP[i] = nums[i] + max(DP[i-1], DP[i-2])
            DP[i] = max(DP[i-1], nums[i] + DP[i-2])
            
        return(DP[-1])