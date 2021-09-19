class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # DFS
        
        # adjacency list
        d = collections.defaultdict(list)
        for a, b in dislikes:
            d[a].append(b)
            d[b].append(a)
            
        colors = {i: None for i in range(1,n + 1)}
        
        def dfs(node, color):
            if not colors[node]:
                colors[node] = color
            else:
                return colors[node] == color
            
            for nei in d[node]:
                if not dfs(nei, - color):
                    return False
            return True
        
        for i in range(1, n+1):
            if not colors[i] and not dfs(i, 1):
                return False
        
        return True