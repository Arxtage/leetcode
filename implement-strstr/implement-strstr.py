class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #O(N) pointers
        
        step = len(needle)
        
        for i in range(len(haystack) - step + 1):
            if haystack[i: i + step] == needle:
                return i
        
        return 0 if step == 0 else -1