import random
class Solution:
    # use binary search
    def __init__(self, w: List[int]):
        
        self.array = []
        prefix_sum = 0
        
        for index, weight in enumerate(w):
            prefix_sum += weight
            self.array.append(prefix_sum)

        self.total_weight = prefix_sum
        
    def pickIndex(self) -> int:
        
        index = random.random() * self.total_weight
        
        L, R = 0, len(self.array)
        
        while L < R:
            mid = (L+R)//2
            
            if self.array[mid] < index:
                L = mid + 1
            else:
                R = mid
        return L
                
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()