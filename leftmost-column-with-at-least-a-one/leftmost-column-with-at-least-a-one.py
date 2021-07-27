# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        # BINARY SEARCH! O(ROW*log(COL))
        ROW, COL = binaryMatrix.dimensions()
        
        # case without 1
        count = 0
        for i in range(ROW):
            count += binaryMatrix.get(i, COL-1)
        if count == 0:
            return -1
        
        L, R = 0, COL - 1
        
        while L + 1 < R:            
            if (L + R) % 2 == 0:
                mid = (L + R) // 2
            else:
                mid = (L + R) // 2 + 1
            
            count = 0
            for i in range(ROW):
                if binaryMatrix.get(i, mid):
                    count = 1
                    break
            if count:
                R = mid
            else:
                L = mid
            
        for c in range(L, R + 1):
            for r in range(ROW):
                if binaryMatrix.get(r, c):
                    return(c)

