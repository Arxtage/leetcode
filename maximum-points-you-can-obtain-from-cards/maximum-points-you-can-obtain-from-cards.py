class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # sliding window
        # O(k)
        
        L = 0
        R = len(cardPoints) - k
        
        res = curr_sum = sum(cardPoints[R:])
        
        while R < len(cardPoints):
            curr_sum = curr_sum + cardPoints[L] - cardPoints[R]
            if curr_sum > res:
                res = curr_sum
            L+=1
            R+=1
        return res