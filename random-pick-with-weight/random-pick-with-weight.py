import random
class Solution:

    def __init__(self, w: List[int]):
        
        self.array = []
        prefix_sum = 0
        
        for index, weight in enumerate(w):
            prefix_sum += weight
            self.array.append(prefix_sum)

        self.total_weight = prefix_sum
        
    def pickIndex(self) -> int:
        
        index = random.random() * self.total_weight
        
        for ind, prefix in enumerate(self.array):
            if index < prefix:
                return ind

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()