# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
                
        def isSameTree(p: TreeNode, q: TreeNode) -> bool:
        # DSF
            if not p and not q:
                return(True)
            if not p or not q:
                return(False)

            if p.val != q.val:
                return(False)

            return(isSameTree(p.left,q.left) and isSameTree(p.right,q.right))
        
        def find(node, subNode):
            if node is None: return False
            if isSameTree(node, subNode): return True
            return find(node.left, subNode) or find(node.right, subNode)
            

        return(find(root, subRoot))
    