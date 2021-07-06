class Solution:
    # Use HashMap (dict) 
    # o(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i in range(len(nums)):
            minus = target - nums[i]
            if minus in d.keys():
                return([d[minus],i])
            else:
                d[nums[i]] = i
            