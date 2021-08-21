class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # O(nlogn + mlogm)
        nums1.sort()
        nums2.sort()
        
        ind1 = 0
        ind2 = 0
        
        res = []
        
        while ind1 < len(nums1) and ind2 < len(nums2):
            if nums1[ind1] == nums2[ind2]:
                res.append(nums1[ind1])
                ind1 += 1
                ind2 += 1
            elif nums1[ind1] < nums2[ind2]:
                ind1 += 1
            else:
                ind2 += 1
        return res 
                