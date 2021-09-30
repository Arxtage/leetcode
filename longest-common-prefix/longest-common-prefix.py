class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # choose first word as initial and search for it in other words, decreasing until nothing left or some len left
        
        # O(len(word) * N)
        prefix = strs.pop(0)
        cur_len = len(prefix)
        
        while strs:
            word = strs.pop(0)
            while cur_len > len(word) or prefix != word[:cur_len]:
                prefix = prefix[:-1]
                cur_len = len(prefix)

        return prefix