class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # DP 2D o(n*m)
        DP = [[0 for j in range(n+1)] for i in range(m+1)]
        DP[m-1][n-1] = 1
        
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i == m-1 and j == n-1:
                    DP[i][j] = 1
                else:
                    DP[i][j] = DP[i+1][j] + DP[i][j+1]
                    
        return(DP[0][0])