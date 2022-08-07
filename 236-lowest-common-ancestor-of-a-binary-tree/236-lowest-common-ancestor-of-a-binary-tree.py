# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root):
            if root:
                if root.val == p.val or root.val == q.val:
                    return root
                l = dfs(root.left)
                r = dfs(root.right)
                if l and r:
                    return root
                return l if l else r
            return None
            
        return dfs(root)
