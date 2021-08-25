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
        
        index
        L, R = 0, len(self.array)
        while L < R:
            mid = (L+R)//2
            if (mid-1 in range(len(self.array)) and self.array[mid-1] < index < self.array[mid]) or (mid-1 == -1 and index < self.array[mid]):
                return len(self.array[:int(mid)])
            elif self.array[mid] > index:
                R = mid
            else:
                L = mid
                
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()