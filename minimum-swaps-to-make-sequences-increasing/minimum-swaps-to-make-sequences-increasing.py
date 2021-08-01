class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        # DP O(n)
        n = len(nums1)
        
        # swap = [200000]*n
        # not_swap = [200000]*n
        
        swap = 1
        not_swap = 0
        
        for i in range(1, n):
            curr_swap = n # max
            curr_not_swap = n
            if nums1[i-1] < nums1[i] and nums2[i-1] < nums2[i]:
                curr_swap = swap + 1
                curr_not_swap = not_swap
                
            # cross check, *what if I have NOT swapped/swapped on prev iteration*
            if nums1[i-1] < nums2[i] and nums2[i-1] < nums1[i]:
                curr_swap = min(curr_swap, not_swap + 1)
                curr_not_swap = min(curr_not_swap, swap)
            swap = curr_swap
            not_swap = curr_not_swap
        return min(curr_swap, curr_not_swap)