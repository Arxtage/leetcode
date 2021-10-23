class Solution:
    # O(n)
    def simplePalindrome(self, s, l, r):
        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return (l, r)
        return True
    
    def validPalindrome(self, s: str) -> bool:
        
        l, r = 0, len(s) - 1
        
        if (result := self.simplePalindrome(s, l, r)) == True:
            return True
    
        elif self.simplePalindrome(s, result[0] + 1, result[1]) == True or \
             self.simplePalindrome(s, result[0], result[1] - 1) == True:
            return True
        return False