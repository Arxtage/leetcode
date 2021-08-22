class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS O(N*M)
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        count_islands = 0
        
        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))
            
            directions = [(0,1), (1,0), (-1,0), (0,-1)]
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    rr, cc = row + dr, col + dc
                    if rr in range(rows) and cc in range(cols) and (rr, cc) not in visited and grid[rr][cc] == '1':
                        q.append((rr, cc))
                        visited.add((rr, cc))
                
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    count_islands += 1
                    
        return count_islands