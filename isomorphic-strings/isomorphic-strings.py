class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # O(n)
        map_s_t = collections.defaultdict()
        map_t_s = collections.defaultdict()
        
        for i in range(len(s)):
            if s[i] not in map_s_t and t[i] not in map_t_s:
                map_s_t[s[i]] = t[i]
                map_t_s[t[i]] = s[i]
            elif map_s_t.get(s[i]) != t[i] or map_t_s.get(t[i]) != s[i]:
                return False
        return True
                