class Solution:
    def reverseBits(self, n: int) -> int:
        res = ''
        # n to bits and reverse
        for i in range(32,-1,-1):

            if n - 2**i >=0:
                res = "1" + res
                n = n - 2**i
            else:
                res = "0" + res

        
        # convert back bits
        fin = 0
        for i in range(len(res)):
            if int(res[i]):
                fin +=2**(len(res) - int(i)-2)
        return(fin)