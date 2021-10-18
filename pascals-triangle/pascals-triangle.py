class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # DP O(n^2)
        
        triangle = [[1 for i in range(j)] for j in range(1, numRows + 1)]
        
        for j in range(2, numRows):
            for i in range(1, j):
                triangle[j][i] = triangle[j - 1][i - 1] + triangle[j - 1][i]
        return triangle