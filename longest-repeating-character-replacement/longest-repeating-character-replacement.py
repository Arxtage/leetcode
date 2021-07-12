class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # o(n)
        hashmap = {}
        maxfreq = 0
        res = 0
        L = 0
        
        for R in range(len(s)):
            
            if s[R] in hashmap.keys():
                hashmap[s[R]] += 1
            else:
                hashmap[s[R]] = 1
                
            maxfreq = max(maxfreq, hashmap[s[R]])
                    
            while (R - L + 1) - maxfreq > k:
                hashmap[s[L]] -= 1
                L += 1
                
            res = max(res, R - L + 1)
        return(res)
        
        
        
            