class Solution:
    def trap(self, height: List[int]) -> int:
        # O(N) O(1)
        # we can trap at each i position min(max_left, max_right) - height[i] water
        # we need max_left and max_right to each position
        
        max_left = 0
        max_right = 0
        
        L, R = 0, len(height) - 1
        
        res = 0
        while L <= R:
            if max_left <= max_right:
                # compute on L and shift
                count = max_left - height[L]
                if count > 0: 
                    res += count
                L += 1
                max_left = max(max_left, height[L - 1])
            else:
                count = max_right - height[R]
                if count > 0:
                    res += count
                R -= 1
                max_right = max(max_right, height[R + 1])
        return res