class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        # O(n) to create hashset
        unique_candy = set(candyType)
        return min(len(unique_candy) , len(candyType)//2)