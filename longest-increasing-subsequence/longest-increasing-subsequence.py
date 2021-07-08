class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # DP o(n^2)
        l = [1]*len(nums)
        
        for ind in range(1, len(l)):
            subproblems = []
            for k in range(ind):
                if nums[k] < nums[ind]:
                    l[ind] = max(l[ind], 1 + l[k])
        return max(l)