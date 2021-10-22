class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # O(n)

        for k in range(1, len(s)//2 +1):   
            if s == s[k:] + s[:k]:
                return True
        return False
                
            
            