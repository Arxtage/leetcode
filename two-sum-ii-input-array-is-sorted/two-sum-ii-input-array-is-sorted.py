class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
       # O(n) two pointers
        L, R = 0, len(numbers) - 1
        
        while L < R:
            
            if numbers[L] + numbers[R] == target:
                return [L +1, R + 1]
            elif numbers[L] + numbers[R] < target:
                L += 1
            else:
                R -= 1
        