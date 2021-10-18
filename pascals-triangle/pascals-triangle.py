class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # DP O(n^2)
        
        triangle = []
        for j in range(numRows):
            row = [1] * (j+1)
            for i in range(1, j):
                row[i] = triangle[j - 1][i - 1] + triangle[j - 1][i]
            triangle.append(row)
                
        return triangle