class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # DFS o(numCOruses + prerequisites)
        
        
        # make graph out of prerequisites
        graph = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            graph[course].append(pre)
        
        visitSet = set()
        
        # can I complete val course
        def dfs(val):
            if val in visitSet:
                return(False)
            
            if graph[val] == []:
                return(True)
            
            visitSet.add(val)
            for neigh in graph[val]:
                if not dfs(neigh):
                    return(False)
            visitSet.remove(val)
            # remove all prereqs
            graph[val] = []
            return(True)
        
        # call for every course node
        for val in (range(numCourses)):
            if not dfs(val):
                return False
        return(True)
       