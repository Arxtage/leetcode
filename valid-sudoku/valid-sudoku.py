class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # O(9*9)
        
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)
        
        
        for i in range(9):
            for j in range(9):
                if board[i][j] =='.':
                    continue
                val = int(board[i][j])
                if 1 <= val <= 9:
                    
                    if val not in rows[i]:
                        rows[i].add(val)
                    else:
                        return(False)
                    
                    if val not in cols[j]:
                        cols[j].add(val)
                    else:
                        return(False)
                    
                    if val not in boxes[(i//3, j//3)]:
                        boxes[(i//3, j//3)].add(val)
                    else:
                        return(False)
        return True
    