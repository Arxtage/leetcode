class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(32,-1,-1):
            if n - 2**i >= 0:
                count+=1
                n = n - 2**i
        return(count)
                
                
