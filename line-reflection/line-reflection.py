class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        # ~ O(n)
        
        # key is y (horisontal line)
        # value is a set of x-s with this y
        hashmap = collections.defaultdict(set) # y : set(x_i,..)
        
        # edge case when point has x=0
        manual_check = []
        
        for point in points:
            if point[0] == 0:
                manual_check.append(point[1])
            hashmap[point[1]].add(point[0])

        # use first point as a hypothesis
        hypothesis = sum(hashmap[points[0][1]]) / len(hashmap[points[0][1]])
        
        for y in manual_check:
            summ = 0
            for x in hashmap[y]:
                summ += x - hypothesis
            if summ != 0:
                return False
            
        for key, val in hashmap.items():
            if sum(val)/len(val) != hypothesis:
                return False
        return True
        