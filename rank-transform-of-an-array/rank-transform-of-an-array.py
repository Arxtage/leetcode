class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # O(n)
        
        hashmap = collections.defaultdict(int)
        
        arr_sorted = sorted(list(set(arr)))
        
        for i in range(len(arr_sorted)):
            hashmap[arr_sorted[i]] = i + 1
        
        for i in range(len(arr)):
            arr[i] = hashmap[arr[i]]
        
        return arr