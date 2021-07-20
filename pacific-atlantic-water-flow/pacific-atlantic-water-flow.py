class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # o(N*M)
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        
        def dfs(r, c, oceanSet, prevHeight):
            
            # less than prevHeight bcs going from oceans uphill
            if ((r,c) in oceanSet or r < 0
                or r == ROWS or c < 0 or c == COLS
                or heights[r][c] < prevHeight):
                return None
            
            oceanSet.add((r, c))
            dfs(r + 1, c, oceanSet, heights[r][c])
            dfs(r - 1, c, oceanSet, heights[r][c])
            dfs(r, c + 1, oceanSet, heights[r][c])
            dfs(r, c - 1, oceanSet, heights[r][c])
            
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
        
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])
        
        res = []
        for r, c in pac & atl:
            res.append([r,c])
        return(res)