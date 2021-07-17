class Solution:
    # o(n^2)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
    
        res = []
#         def twoSum(numbers: List[int], target: int) -> List[int]:
#             L = 0
#             R = len(numbers) - 1

#             while L < R:
#                 if numbers[L] + numbers[R] - target > 0:
#                     R-=1
#                 elif numbers[L] + numbers[R] - target < 0:
#                     L+=1
#                 elif numbers[L] + numbers[R] - target == 0:
#                     res.append([numbers[L], numbers[R], -target])
#                     L+=1
#                     while nums[L] == nums[L-1]:
#                         L+=1
                
        
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            # twoSum(numbers = nums[:i] + nums[i+1:], target = - nums[i])
            
            L = i+1
            R = len(nums) - 1

            while L < R:
                if nums[L] + nums[R] + nums[i] > 0:
                    R-=1
                elif nums[L] + nums[R] + nums[i] < 0:
                    L+=1
                elif nums[L] + nums[R] + nums[i] == 0:
                    res.append([nums[i], nums[L], nums[R]])
                    L+=1
                    while nums[L] == nums[L-1] and L < R:
                        L+=1
        return(res)