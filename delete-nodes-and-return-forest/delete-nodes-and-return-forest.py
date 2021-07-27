# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        # O(N)
        res = []
        to_delete_set = set(to_delete)
            
        def dfs(node, parent_exist):
            
            if not node:
                return None
            
            # append
            if node.val in to_delete_set:
                node.left = dfs(node.left, parent_exist=False)
                node.right = dfs(node.right, parent_exist=False)
                return None 
            else:
                if not parent_exist:
                    res.append(node)
                node.left = dfs(node.left, parent_exist=True)
                node.right = dfs(node.right, parent_exist=True)
                return node
            
        dfs(root,  parent_exist = False)
        return(res)