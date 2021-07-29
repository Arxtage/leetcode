class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        res = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
        
           # O(n) two pointers of Two Nums II
            L, R = i + 1, len(nums) - 1

            while L < R:

                triplet_sum = nums[i] + nums[L] + nums[R]
                if triplet_sum < 0:
                    L += 1
                elif triplet_sum > 0:
                    R -=1
                else:
                    res.append([nums[i], nums[L], nums[R]])
                    L+=1
                    R-=1
                    while nums[L] == nums[L-1] and L < R:
                        L+=1
        return(res)
    
    
