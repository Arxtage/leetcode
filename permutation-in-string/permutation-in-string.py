class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # O()
        # Use two counter dicts
        
        L, R = 0, len(s1) - 1
        
        s1_d = collections.Counter(s1)
        s2_d = collections.Counter(s2[L:R + 1])
        
        while R < len(s2):
                
            if s1_d == s2_d:
                return True
            
            L += 1
            R += 1
            
            if R < len(s2):
                s2_d[s2[R]] += 1
            
            if s2_d[s2[L - 1]] != 1:
                s2_d[s2[L - 1]] -= 1
            else:
                del s2_d[s2[L - 1]]
            
        return False
