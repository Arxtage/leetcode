class Solution:
    def mySqrt(self, x: int) -> int:
    # Bin Search O(logX)
        L, R = 0, x + 1

        while L + 10 < R:
            mid = (L+R) // 2
            val = mid*mid
            if val <= x:
                L = mid
            if val > x:
                R = mid
        for i in reversed(range(L, R)):
            if i*i <= x:
                return(i)
