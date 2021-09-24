class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # Two pointers
        # O(N) O(N)
        res = [None]*len(nums)
        
        i = 0
        j = 0
        while j + len(nums)//2 < len(nums):
            res[i] = nums[j]
            res[i+1] = nums[j + len(nums)//2]
            
            i += 2
            j += 1
        return res