class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # O(order + s)
        
        res = ''
        hashMap = {}
        
        for i in range(len(s)):
            if s[i] in hashMap.keys():
                hashMap[s[i]] += 1
            else:
                hashMap[s[i]] = 1
        
        for val in order:
            if val in hashMap.keys():
                res += hashMap[val] * val
                hashMap.pop(val)
        for key, val in hashMap.items():
            res +=  key*val
            
        return(res)
        