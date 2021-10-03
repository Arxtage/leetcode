class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        # evetything to max of intersecting row&col
        # O(n^2)
        
        # get mins
        row_maxes = [max(row) for row in grid]
        col_maxes = [max(col) for col in zip(*grid)] # transposed

        return sum(min(row_maxes[r], col_maxes[c]) - val
                   for r, row in enumerate(grid)
                   for c, val in enumerate(row))