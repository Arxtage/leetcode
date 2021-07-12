class Solution:
    # middle out
    def countSubstrings(self, s: str) -> int:
        L = 0
        R = 0
        count = 0
        
        def check(count, i, L, R):
            if (i-L < 0) or (i+R >= len(s)):
                return(count)
            if s[i-L] == s[i+R]:
                count += 1
                L+=1
                R+=1
                count = check(count, i, L, R)
            return(count)

        for i in range(len(s)):
            L, R = 0, 0
            count = check(count, i, L, R)
            L, R = 0, 1
            count = check(count, i, L, R)
        return(count)