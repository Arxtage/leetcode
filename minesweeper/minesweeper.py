class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        # DFS O(ROWS*COLS)
        
        if board[click[0]][click[1]] =='M':
            board[click[0]][click[1]] = 'X'
            return board
        
        ROWS, COLS = len(board), len(board[0])
                
        step_list = [[0,1],[1,0],[1,1],[-1,0],[0,-1],[-1,-1],[1,-1],[-1,1]]
        
        # visited = set()
        
        def dfs(r, c, count_bomb):

            if board[r][c] != 'E':
                # visited.add((r, c))
                return
            
            for step in step_list:
                cr, cc = r + step[0], c + step[1]
                if 0 <= cr < ROWS and 0 <= cc < COLS and board[cr][cc] =='M':
                    count_bomb += 1
            
            if not count_bomb:
                board[r][c] = 'B'
                # visited.add((r,c))
            else:
                board[r][c] = str(count_bomb)
                # visited.add((r,c))
                return
                
            for step in step_list:
                cr, cc = r + step[0], c + step[1]
                if 0 <= cr < ROWS and 0 <= cc < COLS: #and (cr, cc) not in visited:
                    dfs(cr, cc, 0)
            
            
        dfs(click[0], click[1], 0)
        return board