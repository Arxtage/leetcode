class Solution:
    def longestPalindrome(self, s: str) -> str:
            
        l = r = 0 
        result = ''
        max_len = 0
        for i in range(len(s)):
            l = r = i
            while l>=0 and r<len(s) and s[l] == s[r]:
                if (r-l+1) > max_len:
                    result = s[l:r+1]
                    max_len = r-l+1
                l-=1
                r+=1
        
            # even case
            l = i
            r = i+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                if (r-l+1) > max_len:
                    result = s[l:r+1]
                    max_len = r-l+1
                l-=1
                r+=1
        
        return(result)