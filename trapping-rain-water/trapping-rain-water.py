class Solution:
    def trap(self, height: List[int]) -> int:
        # O(N) )(N)
        # we can trap at each i position min(max_left, max_right) - height[i] water
        # we need max_left and max_right to each position
        
        # create max_left and max_right arrays
        
        max_left = [0]*len(height)
        max_right = [0]*len(height)
        
        for i in range(1, len(height)):
            max_left[i] = max(max_left[i-1], height[i-1])
            max_right[len(height) - 1 - i] = max(max_right[len(height) - i], height[len(height) - i])
            
        res = 0
        
        for i in range(len(height)):
            count = min(max_left[i], max_right[i]) - height[i]
            if count > 0:
                res += count
        return res
            