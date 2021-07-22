class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ind_zero = 0
        count_zero = 0
        count = 0
        maxi = 0
        
        i = 0
        while i < len(nums):
            if nums[i] == 1:
                count+=1
                maxi = max(count, maxi)
            else:
                count_zero += 1
                
                if count_zero == 2:
                    count = i - ind_zero
                    count_zero = 1
                else:
                    count +=1
                ind_zero = i # 2
                maxi = max(count, maxi)
            i += 1
        return(maxi)
            
                    