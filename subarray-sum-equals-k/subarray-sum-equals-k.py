class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # O(N)
        # prefix sums
        
        hashmap = collections.defaultdict(lambda:0)
        hashmap[0] += 1
        curr_sum = 0
        res = 0
        for ind in range(len(nums)):
            curr_sum += nums[ind]
            if hashmap[curr_sum - k]:
                res += hashmap[curr_sum - k]
            hashmap[curr_sum] += 1
        return res