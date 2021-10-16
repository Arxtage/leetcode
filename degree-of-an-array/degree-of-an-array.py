class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # O(n)
        
        hashmap = collections.defaultdict(list) # [start_ind, finish_ind, count]
        
        maximum_counts = []
        maximum_count = 0

        for ind in range(len(nums)):
           
            if len(hashmap[nums[ind]]) != 3:
                hashmap[nums[ind]] = [ind, ind, 1]
            else:
                hashmap[nums[ind]][1] = ind
                hashmap[nums[ind]][2] += 1
            
            # update maximum_counts
            if hashmap[nums[ind]][2] > maximum_count:
                maximum_count = hashmap[nums[ind]][2]
                maximum_counts = [nums[ind]]
                
            elif hashmap[nums[ind]][2] == maximum_count:
                maximum_counts.append(nums[ind])
                    
        res = len(nums)

        for val in maximum_counts:
            if hashmap[val][1] - hashmap[val][0] + 1 < res:
                res = hashmap[val][1] - hashmap[val][0] + 1
                
        return res
        