class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # BruteForce O(cols + rows + boxes) VEEERY SLOWWWW
        
        ROWS, COLS = len(board), len(board[0])
        
        
        # check rows
        for i in range(ROWS):
            main_set = set()
            for j in range(COLS):
                if board[i][j] =='.':
                    continue
                val = int(board[i][j])
                if 1 <= val <= 9 and val not in main_set:
                    main_set.add(val)
                else:
                    return(False)
        
        # check cols
        for j in range(COLS):
            main_set = set()
            for i in range(ROWS):
                if board[i][j] =='.':
                    continue
                val = int(board[i][j])
                if 1 <= val <= 9 and val not in main_set:
                    main_set.add(val)
                else:
                    return(False)
        
        # not indluding
        box_indexes = [(0,3,0,3),
                          (0,3,3,6),
                          (0,3,6,9),
                          (3,6,0,3),
                          (3,6,3,6),
                          (3,6,6,9),
                          (6,9,0,3),
                          (6,9,3,6),
                          (6,9,6,9)]
        # check boxes
        for box in box_indexes:
            main_set = set()
            for i in range(box[0], box[1]):
                for j in range(box[2], box[3]):
                    if board[i][j] =='.':
                        continue
                    val = int(board[i][j])
                    if 1 <= val <= 9 and val not in main_set:
                        main_set.add(val)
                    else:
                        return(False)
        return(True)
    