class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # O(n)
        # y = ax + b
        
        coord1 = coordinates[0]
        coord2 = coordinates[1]
            
        if coord2[0] - coord1[0] == 0:
            a = 0
        else:
            a = (coord2[1] - coord1[1]) / (coord2[0] - coord1[0])
        
        # vertical line case:
        if coord1[0] == coord2[0]:
            count_vert = 1
            for ind in range(1, len(coordinates) - 1):
                if coordinates[ind][0] == coordinates[ind + 1][0]:
                    count_vert += 1
            if count_vert == len(coordinates) - 1:
                return True
            return False
        
        # rest of cases
        b = coord1[1] - a * coord1[0]
        print(a, b)
        for coord in coordinates[2:]:
            if coord[1] != a * coord[0] + b:
                return False
        return True
        