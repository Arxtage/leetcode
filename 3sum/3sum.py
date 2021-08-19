class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        
        nums.sort()
        
        for i in range(len(nums)):
            if nums[i] > 0:
                break
                
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            L, R = i+1, len(nums) - 1
            
            while L < R:
                
                # Two Sum II
                triplet_sum = nums[L] + nums[i] + nums[R]
                if triplet_sum < 0:
                    L += 1
                elif triplet_sum > 0:
                    R -= 1
                else:
                    res.append([nums[i], nums[L], nums[R]])
                    L += 1
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
        return(res)