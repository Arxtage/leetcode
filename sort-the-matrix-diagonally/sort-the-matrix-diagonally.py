class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        # ind_col - ind_row is constant for each diagonal
        # O(n^2)
        hashmap = collections.defaultdict(list)
        
        ROWS, COLS = len(mat), len(mat[0])
        
        for i in range(ROWS):
            for j in range(COLS):
                hashmap[j - i].append(mat[i][j])
        hashmap = {key: sorted(val) for key, val in hashmap.items()}
        
        for i in range(ROWS):
            for j in range(COLS):
                mat[i][j] = hashmap[j - i].pop(0)
        
        return mat