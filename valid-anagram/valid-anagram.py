class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # o(n)
        dict1 = dict()
        dict2 = dict()
        for val in s:
            if val in dict1.keys():
                dict1[val]+=1
            else:
                dict1[val] = 1
        for val in t:
            if val in dict2.keys():
                dict2[val]+=1
            else:
                dict2[val] = 1
        
        if dict1 == dict2: return(True)
        else: return(False)