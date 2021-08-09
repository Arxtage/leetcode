class Solution:
    def minSwaps(self, s: str) -> int:
        # O(n)
        countClosing, maxim = 0, 0
        for br in s:
            if br == ']':
                countClosing +=1
            else:
                countClosing -=1
            maxim = max(maxim, countClosing)
        return (maxim + 1)//2