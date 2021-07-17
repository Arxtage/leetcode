class Solution:
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # o(nlogn)
        
        intervals.sort()
        res = []
        res.append(intervals[0])
        i = 1
        while i < len(intervals):
            # case 2
            if res[-1][1] < intervals[i][0]:
                res.append(intervals[i])
            # case 1
            elif intervals[i][0] <= res[-1][1] and res[-1][1]  <= intervals[i][1]:
                res[-1] = [res[-1][0], intervals[i][1]]
                
            #case 3 can be skipped
            # elif  intervals[i][1] < res[-1][1]:
            #     pass
            i+=1
        return(res)
            