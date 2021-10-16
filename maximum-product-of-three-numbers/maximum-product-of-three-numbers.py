class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # O(N) 
        
        largest = heapq.nlargest(3, nums) #O(n * log(3))
        smallest = heapq.nsmallest(2, nums) # O(n * log(2))
        
            
        return max(smallest[0] * smallest[1] * largest[0],
                   largest[0] * largest[1] * largest[2])