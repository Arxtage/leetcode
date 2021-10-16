class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # O(n) two pass with counter
        
        hashmap = collections.Counter(nums) # o(n)
        
        res = 0
        curr = 0
        
        for val in nums:
            if val + 1 in hashmap.keys():
                curr = hashmap[val] + hashmap[val + 1]
                if curr > res:
                    res = curr
            curr = 0
            
        return res
            