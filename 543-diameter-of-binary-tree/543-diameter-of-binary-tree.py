# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_depth = 0
        def depth(root):
            if not root:
                return -1
            return 1 + max(depth(root.left),depth(root.right))
        def dfs(root):
            if root:
                lp = depth(root.right)
                rp = depth(root.left)
                self.max_depth = max(2+lp+rp,lp,rp,self.max_depth)
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        return self.max_depth