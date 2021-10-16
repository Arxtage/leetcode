class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # O(N) with heap
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)
        else:
            return heapq.nlargest(3, nums)[2]
    
    
    
#     def thirdMax(self, nums: List[int]) -> int:
#         # O(N)
        
#         maxim = nums.pop(nums.index(max(nums)))
#         third_max = maxim
        
#         iterations = 0
#         while iterations < 2 and len(nums) > 0:
#             new = nums.pop(nums.index(max(nums)))
            
#             if maxim != new:
#                 maxim = new
#                 iterations += 1
            
#             else:
#                 continue
                
#         return third_max if iterations == 1 else maxim