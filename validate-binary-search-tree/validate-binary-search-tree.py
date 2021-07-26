# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # O(N)
        def dfs(node, minim = -math.inf, maxim = math.inf):
            
            if not node:
                return True
            
            if node.val <= minim or node.val >= maxim:
                return False
            
            return(dfs(node.left, minim, node.val) and
                   dfs(node.right, node.val, maxim))
        
        return dfs(root)