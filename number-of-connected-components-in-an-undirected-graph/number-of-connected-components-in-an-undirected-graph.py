class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
#       O(E + V)
        hmap = {i:[] for i in range(n)}
        for edge in edges:
            hmap[edge[0]].append(edge[1])
            hmap[edge[1]].append(edge[0])
            
        visited = set()
        def dfs(node):
            # base returns:
            if node in visited:
                return
            visited.add(node)
            if hmap[node] != []:
                for nei in hmap[node]:
                    dfs(nei)

        count = 0
        for node in range(n):
            if len(visited) == n: 
                break
            if node not in visited:
                dfs(node)
                count += 1
        return(count)
        
        