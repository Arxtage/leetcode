class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Dynamic Programming o(amount * n)
        # dp[0], dp[1], ...., dp[amount]
        
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        for am in range(amount + 1):
            for coin in coins:
                if am - coin >= 0:
                    dp[am] = min(dp[am], 1 + dp[am - coin])
                    
        return dp[amount] if dp[amount] != amount + 1 else -1