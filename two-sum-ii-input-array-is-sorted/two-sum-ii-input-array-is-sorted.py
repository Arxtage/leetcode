class Solution:
    # Use HashMap (dict) 
    # o(n)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = dict() # val : index
        for i in range(len(numbers)):
            minus = target - numbers[i]
            if minus in d.keys():
                return([d[minus]+1,i+1])
            else:
                d[numbers[i]] = i
            
        