class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(n) using set()
        if not nums:
            return 0
        
        nSet = set(nums)
        maxi = 1
        for num in nSet:
            # save time by not checking shorter sequences - we should start from the first element from the resulting sequence
            if num - 1 not in nSet: 
                count = 1
                while num + 1 in nSet:
                    num += 1
                    count += 1
                maxi = max(maxi, count)
        return(maxi)
    
    
        # O(nlogn)  
#         nums.sort()
#         count = 1
#         maxi = 1
#         for i in range(len(nums)-1):
#             if nums[i+1] == nums[i]+1:
#                 count +=1
#             elif nums[i+1] == nums[i]:
#                 continue
#             maxi = max(maxi,count)
#             if nums[i+1] != nums[i]+1:
#                 count = 1
                       
#         return(maxi)
                    