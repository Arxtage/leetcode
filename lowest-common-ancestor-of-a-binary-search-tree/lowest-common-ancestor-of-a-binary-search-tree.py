# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    # Свойство Binary Tree: все что правее больше того что левее
    # если оба меньше current node - то искать в node.left, если больше - в node.right
    # если один меньше/равен другой больше/равен - то это LCA

        if p.val > root.val and q.val > root.val:
            return(self.lowestCommonAncestor(root.right, p, q))
        elif p.val < root.val and q.val < root.val:
            return(self.lowestCommonAncestor(root.left, p, q))
        else:
            return(root)