class Solution:
    # middle out
    def countSubstrings(self, s: str) -> int:

        res = 0
        for i in range(len(s)):
            res += self.check(s, i, 0, 0)
            res += self.check(s, i, 0, 1)
        return(res)

    def check(self, s, i, L, R):
        count = 0
        while (i-L >= 0) and (i+R < len(s)) and s[i-L] == s[i+R]:
            count += 1
            L+=1
            R+=1
        return(count)