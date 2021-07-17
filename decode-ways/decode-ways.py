class Solution:
    def numDecodings(self, s: str) -> int:
        # DP o(n) o(n)
        
        if not s or s[0] == '0':
            return('0')
        
        DP = [0]*(len(s) + 1)
        DP[0], DP[1] = 1, 1
        
        for i in range(2,len(s) + 1):
            
            if s[i-1] == '0':
                if s[i-2] == '1' or s[i-2] == '2':
                    DP[i] = DP[i-2]
                else:
                    return(0)
            elif 10 <= int(s[i-2:i]) <= 26:
                DP[i] = DP[i-1] + DP[i-2]
            else:
                DP[i] = DP[i-1]
                
        return(DP[-1])
                