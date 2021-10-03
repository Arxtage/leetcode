class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Merge sort style O(n + m)
        # O(m) memory
         
        p1 = 0
        p2 = 0
        
        ind = 0
        nums1_cp = nums1[:m]
        
        while p1 < m and p2 < n:
            
            if nums1_cp[p1] < nums2[p2]:
                nums1[ind] = nums1_cp[p1]
                p1 += 1
                
            else:
                nums1[ind] = nums2[p2]
                p2 +=1
            ind += 1
        
            
        while p1 < m:
            nums1[ind] = nums1_cp[p1]
            ind +=1
            p1 += 1
        while p2 < n:
            nums1[ind] = nums2[p2]
            ind +=1
            p2 += 1
            
