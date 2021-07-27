# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # Binary Search O(logn)
        if n == 1:
            return(1)
        
        L, R = 0, n
        res = 1
        while L <= R:
            mid = (L+R) // 2
            res = guess(mid)
            if res ==0:
                return(mid)
            if res  == -1:
                R = mid - 1
            if res == 1:
                L = mid + 1
                
        # return(L)