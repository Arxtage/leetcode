class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        # DP O(n)
        n = len(nums1)
        
        swap = [200000]*n
        not_swap = [200000]*n
        
        swap[0] = 1
        not_swap[0] = 0
        
        for i in range(1, n):
            if nums1[i-1] < nums1[i] and nums2[i-1] < nums2[i]:
                swap[i] = swap[i-1] + 1
                not_swap[i] = not_swap[i-1]
                
            # cross check, *what if I have NOT swapped/swapped on prev iteration*
            if nums1[i-1] < nums2[i] and nums2[i-1] < nums1[i]:
                swap[i] = min(swap[i], not_swap[i-1] + 1)
                not_swap[i] = min(not_swap[i], swap[i-1])
            
        return min(swap[-1], not_swap[-1])