class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        # O(n) find max twice
        
        first_max_ind = nums.index(max(nums))
        first_max = nums.pop(first_max_ind)
        
        second_max = max(nums) if len(nums) > 1 else 0

        return first_max_ind if first_max >= second_max * 2 else -1