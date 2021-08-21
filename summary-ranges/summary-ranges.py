class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # O(n)
        
        res = []
        range_str = ""
        ind = 0
        
        while ind < len(nums):
            
            range_str = str(nums[ind])
            range_end = None
            incr = 1
            while ind + incr < len(nums) and nums[ind + incr] == nums[ind] + incr:
                range_end = str(nums[ind + incr])
                incr += 1
            
            res.append(range_str) if not range_end else res.append(range_str + '->' + range_end)
            ind = ind + incr
        
        return res
        
        