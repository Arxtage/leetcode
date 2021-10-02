class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # O(N)
        
        L = 0
        R = 0
        res = 0
        
        while R < len(nums):
            if nums[R] == val:
                R += 1
            else:
                nums[L] = nums[R]
                res += 1
                L += 1
                R += 1
                
        return res