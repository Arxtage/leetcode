class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # O(max(arr))
        p_arr = 0
        count = 0
        
        for i in range(1, len(arr) + k + 1):
            if p_arr < len(arr) and i != arr[p_arr]:
                count += 1
                if count == k:
                    return i
                continue
            elif p_arr >= len(arr):
                break
            else:
                p_arr += 1
        while count < k:
            i+=1
            count+=1
        return i - 1