# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_depth = 0
        def dfs(root):
            if not root:
                return -1
            lp = dfs(root.left)
            rp = dfs(root.right)
            self.max_depth = max(2+lp+rp,lp,rp,self.max_depth)
            return 1 + max(lp,rp)
        dfs(root)
        return self.max_depth