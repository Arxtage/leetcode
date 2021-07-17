class Solution:
    # Use Two Pointers
    # o(n)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
            
        L = 0
        R = len(numbers) - 1
        
        while True:
            if numbers[L] + numbers[R] > target:
                R-=1
            elif numbers[L] + numbers[R] < target:
                L+=1
            elif numbers[L] + numbers[R] == target:
                return([L+1, R+1])