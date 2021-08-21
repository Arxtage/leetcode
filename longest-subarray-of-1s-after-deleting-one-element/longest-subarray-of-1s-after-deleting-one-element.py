class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # O(n)

        result = 0
        curr_max = 0
        zero_ind = None
        for ind in range(len(nums)):
            if nums[ind] == 0:
                # first time 0
                if zero_ind is None:
                    zero_ind = ind
                else:
                    result = max(result, curr_max)
                    curr_max = ind - zero_ind - 1
                    zero_ind = ind
            else:
                curr_max += 1
        result = max(result, curr_max)
        
        # must delete element
        if zero_ind is None:
            return result - 1
        return result
            
        