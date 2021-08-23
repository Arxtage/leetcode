class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # O(N) O(len(p))
        # Two pointers and counter dict
        
        res = []
        
        if len(p) > len(s):
            return res
        
        L, R = 0, len(p)
        
        counter_p = collections.Counter(p)
        counter_s = collections.Counter(s[L:R])
        
        while R < len(s) + 1:
            
            if counter_p == counter_s:
                res.append(L)
            
            #delete first
            if counter_s[s[L]] >1:
                counter_s[s[L]] -= 1
            else:
                del counter_s[s[L]]
            
            # add next
            if R < len(s):
                counter_s[s[R]] += 1
                
            L += 1
            R += 1
            
            
        return res