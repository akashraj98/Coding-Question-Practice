# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = [] 
        def dfs(root):
            if root:
                dfs(root.left)
                if low <= root.val and root.val <= high:
                    res.append(root.val)
                dfs(root.right)

        dfs(root)
        return sum(res)