class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(nlogn)
        if not nums:
            return 0
        
        nums.sort()
        count = 1
        maxi = 1
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]+1:
                count +=1
            elif nums[i+1] == nums[i]:
                continue
            maxi = max(maxi,count)
            if nums[i+1] != nums[i]+1:
                count = 1
                       
        return(maxi)