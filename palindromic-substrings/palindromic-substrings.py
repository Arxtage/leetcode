class Solution:
    # middle out
    def countSubstrings(self, s: str) -> int:

        res = 0
        for i in range(len(s)):
            res += self.check(s, i, i)
            res += self.check(s, i, i + 1)
        return(res)

    def check(self, s, L, R):
        count = 0
        while (L >= 0) and (R < len(s)) and s[L] == s[R]:
            count += 1
            L-=1
            R+=1
        return(count)