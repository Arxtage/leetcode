class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # using sort o(n*logn*m) where n - avg len of word, m - num of strings
        d = {}
        for str in strs:
            tmp = ''.join(sorted(str))
            if tmp in d.keys():
                d[tmp].append(str)
            else:
                d[tmp] = [str]
        return(list for list in d.values())