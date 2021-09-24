class SparseVector:
    def __init__(self, nums: List[int]):
        self.non_zero = {ind: nums[ind] for ind in range(len(nums)) if nums[ind]}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        dot_prod = 0
        
        for key in self.non_zero:
            if key in vec.non_zero:
                dot_prod += self.non_zero[key] * vec.non_zero[key]
            
        return dot_prod

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)