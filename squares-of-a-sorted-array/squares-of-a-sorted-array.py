class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # O(N)
        res = [0]*len(nums)
        
        L, R = 0, len(nums) - 1
        
        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[L]) <= abs(nums[R]):
                val = nums[R]
                R -= 1
            else:
                val = nums[L]
                L += 1
            res[i] = val * val
        return(res)
            