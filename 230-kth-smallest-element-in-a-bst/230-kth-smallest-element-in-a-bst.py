# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []
        def dfs(root):
            if root:
                dfs(root.left)
                ans.append(root.val)
                dfs(root.right)
        dfs(root)
        return ans[k-1]