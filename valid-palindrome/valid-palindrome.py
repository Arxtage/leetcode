class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove punkt, lower and remove whitespaces
        s = re.sub(r'[^\w\s]','',s.lower().replace(" ", "").replace("_", ""))
        L = 0
        R = len(s)-1
        while L < R:
            if s[L] ==s[R]:
                L+=1
                R-=1
            else:
                return(False)
        return(True)
