class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        hashmap = collections.Counter(nums)
        
        res = 0
        for key, val in hashmap.items():
            res += val*(val - 1)//2
        return res