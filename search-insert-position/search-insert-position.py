class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # O(logn) Bin Search
        
        L = 0
        R = len(nums) - 1
        
        while L <= R:
            mid = (L + R)//2
            if nums[mid] < target:
                L = mid + 1
            elif nums[mid] > target:
                R = mid - 1
            elif nums[mid] == target:
                return mid
                
        return L