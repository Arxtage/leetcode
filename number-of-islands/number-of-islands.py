class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # O(N*M)
        ROWS = len(grid)
        COLS = len(grid[0])
        res = 0
        def dfs(i, j):
            # bottom-up
            # init returns
            if grid[i][j] == 0 or i < 0 or i == ROWS or j < 0 or j == COLS:
                return
            if i + 1 < ROWS and grid[i + 1][j] =='1':
                grid[i + 1][j] = '0'
                dfs(i + 1, j)
                
            if i - 1 >= 0 and grid[i - 1][j] =='1':
                grid[i - 1][j] = '0'
                dfs(i - 1, j)
                
            if j + 1 < COLS and grid[i][j + 1] =='1':
                grid[i][j + 1] = '0'
                dfs(i, j + 1)
                
            if j - 1 >= 0 and grid[i][j - 1] =='1':
                grid[i][j - 1] = '0'
                dfs(i, j - 1)
                
            grid[i][j] = '0'
            return
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1':
                    res+=1
                    dfs(i, j)
        return(res)