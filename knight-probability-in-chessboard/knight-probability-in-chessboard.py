class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # DP solution O(N^2*k)

        def possibleMoves(pos, n):
            q = []
            if 0 <= pos[0] + 1 and pos[0] + 1 < n and 0 <= pos[1] + 2 and pos[1] + 2 < n:
                q.append([pos[0] + 1, pos[1] + 2])
            if 0 <= pos[0] + 2 and pos[0] + 2 < n and 0 <= pos[1] + 1 and pos[1] + 1 < n:
                q.append([pos[0] + 2, pos[1] + 1])
            if 0 <= pos[0] + 2 and pos[0] + 2 < n and 0 <= pos[1] - 1 and pos[1] - 1 < n:
                q.append([pos[0] + 2, pos[1] - 1])
            if 0 <= pos[0] + 1 and pos[0] + 1 < n and 0 <= pos[1] - 2 and pos[1] - 2 < n:
                q.append([pos[0] + 1, pos[1] - 2])


            if 0 <= pos[0] - 1 and pos[0] - 1 < n and 0 <= pos[1] + 2 and pos[1] + 2 < n:
                q.append([pos[0] - 1, pos[1] + 2])
            if 0 <= pos[0] - 2 and pos[0] - 2 < n and 0 <= pos[1] + 1 and pos[1] + 1 < n:
                q.append([pos[0] - 2, pos[1] + 1])
            if 0 <= pos[0] - 2 and pos[0] - 2 < n and 0 <= pos[1] - 1 and pos[1] - 1 < n:
                q.append([pos[0] - 2, pos[1] - 1])
            if 0 <= pos[0] - 1 and pos[0] - 1 < n and 0 <= pos[1] - 2 and pos[1] - 2 < n:
                q.append([pos[0] - 1, pos[1] - 2])
            return(q)
            
        board = [[0 for i in range(n)] for j in range(n)]
        
        board[row][column] = 1 # initial probability
        
        for _ in range(k):
            newboard = [[0 for i in range(n)] for j in range(n)]
            for r in range(n):
                for c in range(n):
                    moves = possibleMoves([r, c], n)
                    for pos in moves:
                        newboard[r][c] += board[pos[0]][pos[1]] * 1/8
            
            board = newboard
            
        res = 0
        
        for i in range(n):
            for j in range(n):
                res += board[i][j]
        return(res)
        
# WORKS BUT TOO INEFFICIENT
# class Solution:
#     def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
#         # O(8^k)
#         if k == 0:
#             return(1)
        
#         probability = 0
#         iterNum = 0
        
#         q = collections.deque([[row, column]])
#         while q:
#             if iterNum > k:
#                 return(probability/8**k)
#             probability = len(q)
            
#             for i in range(len(q)):
#                 pos = q.popleft()
                
#                 if 0 <= pos[0] + 1 and pos[0] + 1 < n and 0 <= pos[1] + 2 and pos[1] + 2 < n:
#                     q.append([pos[0] + 1, pos[1] + 2])
#                 if 0 <= pos[0] + 2 and pos[0] + 2 < n and 0 <= pos[1] + 1 and pos[1] + 1 < n:
#                     q.append([pos[0] + 2, pos[1] + 1])
#                 if 0 <= pos[0] + 2 and pos[0] + 2 < n and 0 <= pos[1] - 1 and pos[1] - 1 < n:
#                     q.append([pos[0] + 2, pos[1] - 1])
#                 if 0 <= pos[0] + 1 and pos[0] + 1 < n and 0 <= pos[1] - 2 and pos[1] - 2 < n:
#                     q.append([pos[0] + 1, pos[1] - 2])

                
#                 if 0 <= pos[0] - 1 and pos[0] - 1 < n and 0 <= pos[1] + 2 and pos[1] + 2 < n:
#                     q.append([pos[0] - 1, pos[1] + 2])
#                 if 0 <= pos[0] - 2 and pos[0] - 2 < n and 0 <= pos[1] + 1 and pos[1] + 1 < n:
#                     q.append([pos[0] - 2, pos[1] + 1])
#                 if 0 <= pos[0] - 2 and pos[0] - 2 < n and 0 <= pos[1] - 1 and pos[1] - 1 < n:
#                     q.append([pos[0] - 2, pos[1] - 1])
#                 if 0 <= pos[0] - 1 and pos[0] - 1 < n and 0 <= pos[1] - 2 and pos[1] - 2 < n:
#                     q.append([pos[0] - 1, pos[1] - 2])
                
#             iterNum += 1
#         return(0)