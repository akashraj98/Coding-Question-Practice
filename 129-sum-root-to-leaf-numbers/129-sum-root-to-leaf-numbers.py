# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(root,ans=""):
            if root:
                ans+= str(root.val)
                if not root.left and not root.right:
                    nonlocal res
                    res+= int(ans)
                dfs(root.left,ans)
                dfs(root.right,ans)
        dfs(root)
        return res
        
                    
        