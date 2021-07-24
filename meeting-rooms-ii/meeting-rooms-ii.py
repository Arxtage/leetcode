class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # O(N^2) worth case when all lectures are at the same time. O(N*Output) 
        
        intervals.sort()
        maxi = 1
        rooms = [intervals[0][1]]
        
        for interv in intervals[1:]:
            for i in range(len(rooms)):
                if rooms[i] <= interv[0]:
                    rooms[i] = interv[1]
                    break
                if i == (len(rooms) - 1):  
                    rooms.append(interv[1])
            maxi = max(maxi, len(rooms))
        return(maxi)