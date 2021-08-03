class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        # Backtracking
        """
        Do not return anything, modify board in-place instead.
        """
        
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)
        
        for i in range(9):
            for j in range(9):
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                boxes[(i//3, j//3)].add(board[i][j])
                
        list_of_candidates = ['1','2','3','4','5','6','7','8','9']
        
        def is_valid(i, j, val):
            
            if val in rows[i] or val in cols[j] or val in boxes[(i//3, j//3)]:
                return(False)
            return(True)

        
        def place(i, j, val):
            board[i][j] = val
            rows[i].add(val)
            cols[j].add(val)
            boxes[(i//3, j//3)].add(val)
        
        def remove(i, j, val):
            board[i][j] = '.'
            rows[i].remove(val)
            cols[j].remove(val)
            boxes[(i//3, j//3)].remove(val)
            
        def backtrack(i, j):
            if i == 8 and j == 9:
                return True
            elif j == 9:
                j = 0
                i += 1

            # iterate all possible candidates.
            if board[i][j] != '.':
                return backtrack(i, j + 1)
                
            for val in list_of_candidates:
                if is_valid(i, j, val):
                    
                    # try this partial candidate solution
                    place(i, j, val)
                    
                    # given the candidate, explore further.
                    if backtrack(i, j + 1):
                        return True
                    
                    # backtrack
                    remove(i, j, val)

            return False
            
            
        backtrack(0,0)
        