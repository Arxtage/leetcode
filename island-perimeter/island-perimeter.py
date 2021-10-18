class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # DFS # O(m*n) worth case, but O(k) on average where k - num of land cells
        
        def dfs(row, col):
            nonlocal perimeter
            # base
            if (row, col) in visited:
                return
            
            if ROWS <= row or row < 0  or COLS <= col or col < 0 or grid[row][col] == 0:
                perimeter += 1
                return
        
            visited.add((row, col))
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
            return
        
        
        perimeter = 0
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        
        # find the first land
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    dfs(i, j)
                    return perimeter