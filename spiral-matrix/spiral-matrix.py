class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        res = []
        m = len(matrix[0])
        n = len(matrix)
        L = 0
        R = m
        T = 0
        B = n
        
        while len(res) < n*m:
            
            # Right
            res += matrix[T][L:R]
            
            # Down
            for i in range(T+1,B):
                res.append(matrix[i][R-1])
            if len(res) >= n*m:
                break

            # Left
            res += matrix[B-1][R-2:L:-1]
            if len(res) >= n*m:
                break
                
            # Up
            for i in range(B-1,T,-1):
                res.append(matrix[i][L])
            
            L+=1
            T+=1
            R-=1
            B-=1
        
        return(res)