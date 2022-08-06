# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr = []
        def dfs(root):
            if root:
                dfs(root.left)
                curr.append(root.val)
                dfs(root.right)
        dfs(root)
        curr.sort()
        self.i= 0
        def dfs2nd(root):
            if root:
                dfs2nd(root.left)
                if root.val != curr[self.i]:
                    root.val = curr[self.i]
                self.i+=1
                dfs2nd(root.right)
        dfs2nd(root)
        

