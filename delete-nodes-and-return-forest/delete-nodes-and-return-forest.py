# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        # O(N)
        res = []
        to_delete_set = set(to_delete)
        if root.val not in to_delete_set:
            res.append(root)
            
        def dfs(node):
            if not node:
                return
            
            # append
            if node.val in to_delete_set:
                if node.left and node.left.val not in to_delete_set:
                    res.append(node.left)
                if node.right and node.right.val not in to_delete_set:
                    res.append(node.right)
            
            # delete connection
            if node.left and node.left.val in to_delete_set:
                dfs(node.left)
                node.left = None
            if node.right and node.right.val in to_delete_set:
                dfs(node.right)
                node.right = None
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return(res)