class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # O(N)
        
        remainder = 1
        
        for i in reversed(range(len(digits))):
            if digits[i] + remainder >= 10:
                digits[i] = digits[i] + remainder - 10
                remainder = 1
            else:
                digits[i] = digits[i] + remainder
                remainder = 0
        
        if not remainder:
            return digits
        else:
            return [remainder] + digits