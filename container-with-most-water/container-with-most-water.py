class Solution:
    def maxArea(self, height: List[int]) -> int:
        # O(N)
        # two pointers
        L, R = 0, len(height) - 1
        maxx = 0
        
        while L < R:
            
            if height[L] <= height[R]:
                maxx = max(maxx, height[L]*(R - L))
                L+=1
            else:
                maxx = max(maxx, height[R]*(R - L))
                R-=1
        return maxx