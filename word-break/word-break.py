class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        DP = [False]*(len(s)+1)
        DP[-1] = True
        
        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i+len(w)] == w:
                    DP[i] = DP[i+len(w)]
                    
                if DP[i]:
                    break
        return(DP[0])