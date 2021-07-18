class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # equivalent to the problem: Return number of NOT overlapping intervals
        points.sort()
        
        prev = float(-inf)
        res = 0
        for interv in points:
            if interv[0] > prev:
                prev = interv[1]
                res +=1
            else:
                prev = min(prev, interv[1])
        return(res)