# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        # Optimal O(N) worth case, rather O(logN)
        
        successor = None
        
        while root:
            
            if p.val >= root.val:
                root = root.right
            else:
                successor = root
                root = root.left
                
        return(successor)
        
        
        # BruteForce Inorder
        
#         if not root:
#             return(None)
#         res = []
#         def inorder(node):

#             if node.left:
#                 inorder(node.left)

#             res.append(node)

#             if node.right:
#                 inorder(node.right)
            
#         inorder(root)

#         for i in range(len(res)):
#             if res[i].val == p.val and (i + 1 < len(res)):
#                 return(res[i+1])
#         return(None)
                