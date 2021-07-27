class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binary Search o(logn)
        # two cases
        
        L, R = 0, len(nums) -1
        
        # pivot
        while L <= R:
            mid = (L+R) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[L]:
                if nums[L] <= target < nums[mid]:
                    R = mid - 1
                else:
                    L = mid + 1
            else:
                if nums[mid] < target <= nums[R]:
                    L = mid + 1
                else:
                    R = mid - 1
        return(-1)