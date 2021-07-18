class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # o(nlogn)
        intervals.sort()
        prev = float("-inf")
        res = 0
        for interv in intervals:
            if interv[0] >= prev:
                prev = interv[1]
            else:
                res += 1
                prev = min(prev, interv[1])
        return res