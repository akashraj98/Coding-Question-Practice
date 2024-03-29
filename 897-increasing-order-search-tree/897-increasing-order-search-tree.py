# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            if root:
                dfs(root.left)
                root.left = None
                self.curr.right = root
                self.curr = self.curr.right # or root
                dfs(root.right)
        
        dummy = self.curr = TreeNode()
        dfs(root)
        return dummy.right