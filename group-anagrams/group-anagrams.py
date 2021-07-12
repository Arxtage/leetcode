# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         # o()
#         d = {} # dict:list of anagrams
        
#         for str in strs:
#             dict1 = {}
#             for ltr in str:
#                 if ltr in dict1.keys():
#                     dict1[ltr]+=1
#                 else:
#                     dict1[ltr] = 1
#             if dict1 in d.keys():
#                 d[dict1].append(str)
#             else:
#                 d[dict1] = [str]
            
            
#         for key in d.keys():
#             print(d[key])
    
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # using sort
        d = {}
        for str in strs:
            tmp = ''.join(sorted(str))
            if tmp in d.keys():
                d[tmp].append(str)
            else:
                d[tmp] = [str]
        return(list for list in d.values())