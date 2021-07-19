# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # DFS
    def maxDepth(self, root: TreeNode) -> int:
        def dfs (node):
            if not node:
                return(False)
            level = 1 + max(dfs(node.right), dfs(node.left))
            return(level)  
            
            
        return dfs(root) if root else 0