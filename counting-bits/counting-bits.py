class Solution:
    def countBits(self, n: int) -> List[int]:
        # DP o(nlogn)
        # 1 + dp[i - closest]
        # closest from [1,2,4,8,16, ...]

        res = [None] * (n + 1)
        
        # base
        res[0] = 0
        
        closest = 0
        for i in range(1, n + 1):
            if log2(i).is_integer():
                closest = i
            res[i] = 1 + res[i - closest]
        return(res)
            