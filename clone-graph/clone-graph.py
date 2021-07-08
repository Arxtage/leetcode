"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        hashmap = {} # map old node to new copy
        
        def dfs(node):
            if node.val in hashmap:
                return(hashmap[node.val])
            
            copied_node = Node(node.val)
            hashmap[node.val] = copied_node
            for nei in node.neighbors:
                copied_node.neighbors.append(dfs(nei))
            return(copied_node)
        
        return dfs(node) if node else None
        