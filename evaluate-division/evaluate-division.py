class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # DFS O(N*M)
        
        # create a graph
        graph = {}
        
        for i in range(len(equations)):
            
            if equations[i][0] not in graph:
                graph[equations[i][0]] = {equations[i][1] : values[i]}
            else:
                graph[equations[i][0]][equations[i][1]] = values[i]
                
            if equations[i][1] not in graph:
                graph[equations[i][1]] = {equations[i][0] : 1/values[i]}
            else:
                graph[equations[i][1]][equations[i][0]] = 1/values[i]

        
        def dfs(start, end, multiple, visited):
            # base
            if start not in graph or end not in graph or start in visited:
                return -1
            
            for key, val in graph[start].items():
                if end == key:
                    multiple *= val
                    return multiple
                else:
                    visited.add(start)
                    # print(visited)
                    res = dfs(key, end, multiple * val, visited)
                    if res != -1:
                        return res
            return(-1)
        
        
        calculations = []
        for query in queries:
            visited = set()
            calculations.append(dfs(query[0], query[1], 1, visited))
            
        return(calculations)
            