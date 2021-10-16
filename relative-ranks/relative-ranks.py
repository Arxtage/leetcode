class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # O(nlogn)
        
        scores_sorted = sorted([[val, ind] for ind, val in enumerate(score)], reverse = True)
        
        k = 0
        for val, ind in scores_sorted:
            if k == 0:
                score[ind] = 'Gold Medal'
            elif k == 1:
                score[ind] = 'Silver Medal'
            elif k == 2:
                score[ind] = 'Bronze Medal'
            else:
                score[ind] = str(k + 1)
            k += 1
        return score