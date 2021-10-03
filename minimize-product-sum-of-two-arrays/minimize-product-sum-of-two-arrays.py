class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        # O(nlogn) 
        nums1.sort()
        nums2.sort(reverse = True)
        return sum([nums1[ind] * nums2[ind] for ind in range(len(nums1))])