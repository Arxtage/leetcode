class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # O(N) brute
        
        L = -1
        R = -1
        
        for i in range(len(nums)):
            if nums[i] == target:
                if L < 0:
                    L = i
                    R = i
                elif L >= 0:
                    R = i
            elif L >= 0 and R >= 0 and nums[i] != target:
                break
        return [L, R]