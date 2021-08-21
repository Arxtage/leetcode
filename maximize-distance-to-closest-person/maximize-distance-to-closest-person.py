class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        # O(N)
        # two pointers
        
        L, R = 0, 0
        
        result = 0
        
        # in case of open start:
        while seats[R] != 1:
            R += 1
        result = max(result, R)
        L = R
        
        while R < len(seats):
            if seats[R] == 1:
                sub = R - L
                if sub % 2:
                    sub -= 1
                result = max(result, sub//2)
                L = R
            R += 1
            
        # in case of open end
        if L!= len(seats) - 1:
            result = max(result, len(seats) - L - 1)
        
        return result