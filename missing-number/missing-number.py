class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nset = set(nums)
        for i in range(len(nums) + 1):
            if i not in nset:
                return i 